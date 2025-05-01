from __future__ import annotations
from datetime import datetime

from django.db import models


class SensorManager(models.Manager['Sensor']):
    def is_exists(self, timestamp: datetime) -> bool:
        return self.filter(timestamp=timestamp).exists()

    def find_one_latest(self) -> Sensor | None:
        return self.order_by('-timestamp').first()

    def find_many(self) -> list[Sensor]:
        return list(self.all().order_by('timestamp'))

    def find_many_by_columns(
        self,
    ) -> tuple[list[datetime], list[float], list[float], list[float]]:
        queryset = (
            self.all()
            .order_by('timestamp')
            .values_list(
                'timestamp',
                'temperature',
                'humidity',
                'air_quality',
            )
        )
        timestamp, temperature, humidity, air_quality = zip(*queryset)
        return (
            list(timestamp),
            list(map(float, temperature)),
            list(map(float, humidity)),
            list(map(float, air_quality)),
        )


class Sensor(models.Model):
    timestamp = models.DateTimeField(db_index=True, unique=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    air_quality = models.DecimalField(max_digits=7, decimal_places=2)

    objects = SensorManager()

    def __str__(self) -> str:
        return f'{self.timestamp.isoformat()} <{self.pk}>'
