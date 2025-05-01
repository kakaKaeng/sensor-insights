from datetime import datetime
from unittest.mock import MagicMock

from apps.sensors.services.sensor_process import SensorProcessService


class TestSensorProcess:
    def setup_method(self) -> None:
        mock_repo = MagicMock()
        mock_repo.find_many_by_columns.return_value = (
            [
                datetime(2025, 1, 1, 12, 0, 0),
                datetime(2025, 1, 1, 12, 1, 0),
                datetime(2025, 1, 1, 12, 2, 0),
                datetime(2025, 1, 1, 12, 3, 0),
                datetime(2025, 1, 1, 12, 4, 0),
                datetime(2025, 1, 1, 12, 5, 0),
            ],
            [40, 50, 60, 70, 80, 90],  # temperature
            [42, 58, 63, 77, 85, 240],  # humidity
            [40, 50, 60, 70, 80, 90],  # air_quality
        )

        self.sensor_process_service = SensorProcessService(
            sensor_repo=mock_repo,
        )

    def test_get_iqr(self) -> None:
        iqr = self.sensor_process_service._get_iqr(
            values=[40, 50, 60, 70, 80, 90]
        )
        assert iqr.lower == 5 and iqr.upper == 125

    def test_get_process_data(self) -> None:
        process_data = self.sensor_process_service.get_process_data()
        assert process_data.count == 6
        assert process_data.temperature.iqr_lower == 5
        assert process_data.temperature.iqr_upper == 125

        assert process_data.humidity.iqr_lower == 17.5
        assert process_data.humidity.iqr_upper == 125.5

        assert process_data.air_quality.iqr_lower == 5
        assert process_data.air_quality.iqr_upper == 125

    def test_get_iqr_empty(self) -> None:
        iqr = self.sensor_process_service._get_iqr(values=[40, 50, 60])
        assert iqr.lower is None and iqr.upper is None
