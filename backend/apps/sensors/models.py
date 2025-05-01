from __future__ import annotations
from datetime import datetime

from django.db import models


class SensorManager(models.Manager['Sensor']):
    def is_exists(self, timestamp: datetime) -> bool:
        return self.filter(timestamp=timestamp).exists()

    def find_one_latest(self) -> Sensor | None:
        return self.order_by('-timestamp').first()


class Sensor(models.Model):
    timestamp = models.DateTimeField(db_index=True, unique=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    air_quality = models.DecimalField(max_digits=7, decimal_places=2)

    objects = SensorManager()

    def __str__(self) -> str:
        return f'{self.timestamp.isoformat()} <{self.pk}>'
