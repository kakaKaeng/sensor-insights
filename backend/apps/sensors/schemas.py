from datetime import datetime

from pydantic import BaseModel, field_validator


class SensorCSVData(BaseModel):
    timestamp: datetime
    temperature: float | None
    humidity: float | None
    air_quality: float | None

    @field_validator('temperature', 'humidity', 'air_quality', mode='before')
    @classmethod
    def blank_str_to_none(cls, v: str) -> str | None:
        if v == '':
            return None
        return v

    @field_validator('temperature', mode='after')
    @classmethod
    def round_temperature(cls, v: float | None) -> float | None:
        return round(v, 2) if v else v

    @field_validator('humidity', mode='after')
    @classmethod
    def round_humidity(cls, v: float | None) -> float | None:
        return round(v, 2) if v else v

    @field_validator('air_quality', mode='after')
    @classmethod
    def round_air_quality(cls, v: float | None) -> float | None:
        return round(v, 2) if v else v
