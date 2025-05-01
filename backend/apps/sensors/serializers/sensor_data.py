from typing import Any

from rest_framework import serializers

from apps.sensors.models import Sensor


class SensorDataSerializer(serializers.ModelSerializer):
    temperature = serializers.DecimalField(
        allow_null=True,
        required=False,
        max_digits=5,
        decimal_places=2,
        default=None,
    )
    humidity = serializers.DecimalField(
        allow_null=True,
        required=False,
        max_digits=5,
        decimal_places=2,
        default=None,
    )
    air_quality = serializers.DecimalField(
        allow_null=True,
        required=False,
        max_digits=7,
        decimal_places=2,
        default=None,
    )

    class Meta:
        model = Sensor
        fields = [
            'timestamp',
            'temperature',
            'humidity',
            'air_quality',
        ]

    def validate(self, attrs: dict[str, Any]) -> dict[str, Any]:
        if Sensor.objects.is_exists(timestamp=attrs['timestamp']):
            raise serializers.ValidationError('Duplicate sensor data.')

        if (
            attrs['temperature'] is None
            or attrs['humidity'] is None
            or attrs['air_quality'] is None
        ):
            sensor_latest = Sensor.objects.find_one_latest()

            if sensor_latest is None:
                raise serializers.ValidationError(
                    'No sensor data found. Cannot fill forward data.'
                )

            attrs['temperature'] = (
                sensor_latest.temperature
                if attrs['temperature'] is None
                else attrs['temperature']
            )
            attrs['humidity'] = (
                sensor_latest.humidity
                if attrs['humidity'] is None
                else attrs['humidity']
            )
            attrs['air_quality'] = (
                sensor_latest.air_quality
                if attrs['air_quality'] is None
                else attrs['air_quality']
            )

        return attrs
