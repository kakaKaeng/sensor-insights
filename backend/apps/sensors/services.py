import csv
import io
import logging
from typing import Any

from django.db import transaction
from pydantic import TypeAdapter

from apps.sensors.schemas import SensorData
from apps.sensors.serializers import SensorDataSerializer


class SensorCSVService:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def _read_csv(csv_file: Any) -> list[SensorData]:
        decoded_file = csv_file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        reader = csv.DictReader(io_string)
        return TypeAdapter(list[SensorData]).validate_python(reader)

    def _remove_duplicates(self, sensors: list[SensorData]) -> list[SensorData]:
        _temp_sensors = {}
        for sensor in sensors:
            if sensor.timestamp in _temp_sensors:
                self.logger.debug(
                    'remove duplicate sensor {}'.format(sensor.timestamp)
                )
                continue
            _temp_sensors[sensor.timestamp] = sensor
        new_sensors = list(_temp_sensors.values())
        new_sensors.sort(key=lambda x: x.timestamp)
        return new_sensors

    @staticmethod
    def _patch_missing_data(sensors: list[SensorData]) -> None:
        # use data before to fill forward.
        for i, sensor in enumerate(sensors):
            if sensor.temperature is None:
                sensor.temperature = sensors[i - 1].temperature
            if sensor.humidity is None:
                sensor.humidity = sensors[i - 1].humidity
            if sensor.air_quality is None:
                sensor.air_quality = sensors[i - 1].air_quality

    def import_csv(self, csv_file: Any) -> None:
        self.logger.debug('Start importing csv file')

        sensors = self._read_csv(csv_file=csv_file)
        sensors_cleaned = self._remove_duplicates(sensors=sensors)
        self._patch_missing_data(sensors=sensors_cleaned)

        data = TypeAdapter(list[SensorData]).dump_python(
            sensors_cleaned, mode='json'
        )

        with transaction.atomic():
            serializer = SensorDataSerializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            self.logger.debug('Import sensor data successfully')
