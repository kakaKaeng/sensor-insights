from typing import Any

import pytest

from apps.sensors.models import Sensor
from apps.sensors.serializers import SensorDataSerializer


_MOCK_CREATE_PAYLOAD = {
    'timestamp': '2025-01-01T12:00:00Z',
    'temperature': 25.5,
    'humidity': 60.0,
    'air_quality': 100.0,
}


@pytest.fixture
def mock_sensor(db: Any) -> Sensor:
    serializer = SensorDataSerializer(data=_MOCK_CREATE_PAYLOAD)
    assert serializer.is_valid()
    return serializer.save()


class TestSensorDataSerializer:
    def test_create_sensor_data(self, mock_sensor: Sensor) -> None:
        assert mock_sensor.temperature == 25.5

    def test_duplicate(self, mock_sensor: Sensor) -> None:
        serializer = SensorDataSerializer(data=_MOCK_CREATE_PAYLOAD)
        assert serializer.is_valid() is False

    def test_fill_forward(self, mock_sensor: Sensor) -> None:
        payload = {
            'timestamp': '2025-01-02T12:00:00Z',
        }

        serializer = SensorDataSerializer(data=payload)
        assert serializer.is_valid()
        sensor = serializer.save()

        assert sensor.temperature == mock_sensor.temperature
        assert sensor.humidity == mock_sensor.humidity
        assert sensor.air_quality == mock_sensor.air_quality
