from rest_framework import serializers


class ResponseSensorProcessedDataSerializer(serializers.Serializer):
    value = serializers.ListField(
        child=serializers.FloatField(), read_only=True
    )
    iqr_lower = serializers.FloatField(allow_null=True, read_only=True)
    iqr_upper = serializers.FloatField(allow_null=True, read_only=True)


class ResponseSensorProcessedSerializer(serializers.Serializer):
    count = serializers.IntegerField(read_only=True)
    temperature = ResponseSensorProcessedDataSerializer()
    humidity = ResponseSensorProcessedDataSerializer()
    air_quality = ResponseSensorProcessedDataSerializer()
    timestamp = serializers.ListField(
        child=serializers.DateTimeField(read_only=True)
    )
