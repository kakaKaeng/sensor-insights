import statistics

from rest_framework import serializers

from apps.sensors.schemas import SensorColumn


class SensorAggregatedColumnSerializer(serializers.Serializer):
    mean = serializers.SerializerMethodField()
    median = serializers.SerializerMethodField()
    min = serializers.SerializerMethodField()
    max = serializers.SerializerMethodField()

    class Meta:
        fields = [
            'mean',
            'median',
            'min',
            'max',
        ]

    @staticmethod
    def get_mean(data: list[float]) -> float:
        return statistics.mean(data) if data else 0

    @staticmethod
    def get_median(data: list[float]) -> float:
        return statistics.median(data) if data else 0

    @staticmethod
    def get_min(data: list[float]) -> float:
        return min(data) if data else 0

    @staticmethod
    def get_max(data: list[float]) -> float:
        return max(data) if data else 0


class SensorAggregatedSerializer(serializers.Serializer):
    count = serializers.SerializerMethodField()
    temperature = SensorAggregatedColumnSerializer()
    humidity = SensorAggregatedColumnSerializer()
    air_quality = SensorAggregatedColumnSerializer()

    class Meta:
        fields = [
            'count',
            'temperature',
            'humidity',
            'air_quality',
        ]

    @staticmethod
    def get_count(data: SensorColumn) -> int:
        return len(data.timestamp)
