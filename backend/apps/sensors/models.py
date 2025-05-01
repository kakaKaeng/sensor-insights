from __future__ import annotations
from datetime import datetime, timedelta

from django.db import models
from django.utils import timezone

from apps.sensors.schemas import IntervalOptions


class SensorManager(models.Manager['Sensor']):
    def is_exists(self, timestamp: datetime) -> bool:
        return self.filter(timestamp=timestamp).exists()

    def find_one_latest(self) -> Sensor | None:
        return self.order_by('-timestamp').first()

    def find_many(self) -> list[Sensor]:
        return list(self.all().order_by('timestamp'))

    def find_many_by_columns(
        self,
        interval_options: IntervalOptions = IntervalOptions.ALL_TIME,
    ) -> tuple[list[datetime], list[float], list[float], list[float]]:
        queryset = self.all()

        now = timezone.now()
        if interval_options == IntervalOptions.LAST_1_MINUTE:
            queryset = queryset.filter(
                timestamp__gte=now - timedelta(minutes=1)
            )
        elif interval_options == IntervalOptions.LAST_5_MINUTES:
            queryset = queryset.filter(
                timestamp__gte=now - timedelta(minutes=5)
            )
        elif interval_options == IntervalOptions.LAST_10_MINUTES:
            queryset = queryset.filter(
                timestamp__gte=now - timedelta(minutes=10)
            )
        elif interval_options == IntervalOptions.LAST_1_HOUR:
            queryset = queryset.filter(timestamp__gte=now - timedelta(hours=1))
        elif interval_options == IntervalOptions.LAST_24_HOURS:
            queryset = queryset.filter(timestamp__gte=now - timedelta(hours=24))

        queryset = queryset.order_by('timestamp').values_list(
            'timestamp',
            'temperature',
            'humidity',
            'air_quality',
        )
        timestamp, temperature, humidity, air_quality = (
            zip(*queryset) if queryset else ([], [], [], [])
        )
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
