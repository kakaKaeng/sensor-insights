import numpy

from apps.sensors.models import SensorManager
from apps.sensors.schemas import SensorProcessData, ProcessData, IQR


class SensorProcessService:
    def __init__(self, sensor_repo: SensorManager) -> None:
        self.sensor_repo = sensor_repo

    @staticmethod
    def _get_iqr(values: list[float]) -> IQR:
        q1 = numpy.percentile(values, 25)
        q3 = numpy.percentile(values, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        return IQR(lower=float(lower_bound), upper=float(upper_bound))

    def get_process_data(self) -> SensorProcessData:
        _, temperature, humidity, air_quality = (
            self.sensor_repo.find_many_by_columns()
        )

        temperature_iqr = self._get_iqr(values=temperature)
        humidity_iqr = self._get_iqr(values=humidity)
        air_quality_iqr = self._get_iqr(values=air_quality)

        return SensorProcessData(
            count=len(temperature),
            temperature=ProcessData(
                value=temperature,
                iqr_lower=temperature_iqr.lower,
                iqr_upper=temperature_iqr.upper,
            ),
            humidity=ProcessData(
                value=humidity,
                iqr_lower=humidity_iqr.lower,
                iqr_upper=humidity_iqr.upper,
            ),
            air_quality=ProcessData(
                value=air_quality,
                iqr_lower=air_quality_iqr.lower,
                iqr_upper=air_quality_iqr.upper,
            ),
        )
