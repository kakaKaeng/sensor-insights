from __future__ import annotations
from datetime import datetime
from enum import StrEnum

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


class SensorColumn(BaseModel):
    timestamp: list[datetime]
    temperature: list[float]
    humidity: list[float]
    air_quality: list[float]


class IQR(BaseModel):
    lower: float | None
    upper: float | None

    @classmethod
    def empty(cls) -> IQR:
        return cls(lower=None, upper=None)


class ProcessData(BaseModel):
    value: list[float]
    iqr_lower: float | None
    iqr_upper: float | None


class SensorProcessData(BaseModel):
    count: int
    temperature: ProcessData
    humidity: ProcessData
    air_quality: ProcessData


class IntervalOptions(StrEnum):
    LAST_1_MINUTE = 'last_1_minute'
    LAST_5_MINUTES = 'last_5_minutes'
    LAST_10_MINUTES = 'last_10_minutes'
    LAST_1_HOUR = 'last_1_hour'
    LAST_24_HOURS = 'last_24_hours'
    ALL_TIME = 'all_time'
