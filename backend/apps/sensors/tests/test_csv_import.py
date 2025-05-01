import pytest
from pydantic import TypeAdapter

from apps.sensors.schemas import SensorData
from apps.sensors.services import SensorCSVService

_MOCK_DATA = [
    {
        'timestamp': '2025-01-01T12:00:00Z',
        'temperature': 20,
        'humidity': 20,
        'air_quality': 20,
    },
    {
        'timestamp': '2025-01-01T11:49:03Z',  # order case
        'temperature': 10,
        'humidity': 10,
        'air_quality': 10,
    },
    {
        'timestamp': '2025-01-01T12:00:00Z',  # duplicate
        'temperature': 20,
        'humidity': 20,
        'air_quality': 20,
    },
    {
        'timestamp': '2025-01-01T12:10:00Z',  # missing value
        'temperature': None,
        'humidity': None,
        'air_quality': None,
    },
]


@pytest.fixture
def mock_sensors() -> list[SensorData]:
    return TypeAdapter(list[SensorData]).validate_python(_MOCK_DATA)


class TestCsvImport:
    def setup_method(self) -> None:
        self.sensor_csv_service = SensorCSVService()

    def test_duplicates(self, mock_sensors: list[SensorData]) -> None:
        new_sensors = self.sensor_csv_service._remove_duplicates(mock_sensors)
        assert len(mock_sensors) == 4
        assert len(new_sensors) == 3

    def test_missing_data(self, mock_sensors: list[SensorData]) -> None:
        new_sensors = self.sensor_csv_service._remove_duplicates(mock_sensors)
        assert new_sensors[0].temperature == 10

        self.sensor_csv_service._patch_missing_data(new_sensors)
        assert new_sensors[2].temperature == 20
        assert new_sensors[2].humidity == 20
        assert new_sensors[2].air_quality == 20
