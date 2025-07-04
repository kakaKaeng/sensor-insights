import statistics

from apps.sensors.models import SensorManager
from apps.sensors.schemas import (
    SensorProcessData,
    ProcessData,
    IQR,
    IntervalOptions,
)


class SensorProcessService:
    def __init__(self, sensor_repo: SensorManager) -> None:
        self.sensor_repo = sensor_repo

    @staticmethod
    def _get_iqr(values: list[float]) -> IQR:
        if len(values) < 4:
            return IQR.empty()

        sorted_data = sorted(values)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            lower_half = sorted_data[:mid]
            upper_half = sorted_data[mid:]
        else:
            lower_half = sorted_data[:mid]
            upper_half = sorted_data[mid + 1 :]

        q1 = statistics.median(lower_half)
        q3 = statistics.median(upper_half)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return IQR(lower=float(lower), upper=float(upper))

    def get_process_data(
        self, interval_options: IntervalOptions = IntervalOptions.LAST_5_MINUTES
    ) -> SensorProcessData:
        sensor_column = self.sensor_repo.find_many_by_columns(
            interval_options=interval_options
        )

        temperature_iqr = self._get_iqr(values=sensor_column.temperature)
        humidity_iqr = self._get_iqr(values=sensor_column.humidity)
        air_quality_iqr = self._get_iqr(values=sensor_column.air_quality)

        return SensorProcessData(
            count=len(sensor_column.temperature),
            temperature=ProcessData(
                value=sensor_column.temperature,
                iqr_lower=temperature_iqr.lower,
                iqr_upper=temperature_iqr.upper,
            ),
            humidity=ProcessData(
                value=sensor_column.humidity,
                iqr_lower=humidity_iqr.lower,
                iqr_upper=humidity_iqr.upper,
            ),
            air_quality=ProcessData(
                value=sensor_column.air_quality,
                iqr_lower=air_quality_iqr.lower,
                iqr_upper=air_quality_iqr.upper,
            ),
            timestamp=sensor_column.timestamp,
        )
