from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.commons.permissions import ApiKeyPermission
from apps.sensors.models import Sensor
from apps.sensors.schemas import IntervalOptions
from apps.sensors.serializers.sensor_aggregated import (
    SensorAggregatedSerializer,
)
from apps.sensors.serializers.sensor_data import SensorDataSerializer
from apps.sensors.services.sensor_process import SensorProcessService


class SensorDataApiView(APIView):
    permission_classes = (ApiKeyPermission,)

    def post(self, request: Request) -> Response:
        serializer = SensorDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'message': 'success',
            },
            status=status.HTTP_201_CREATED,
        )


class SensorProcessedApiView(APIView):
    permission_classes = (ApiKeyPermission,)

    def get(self, request: Request) -> Response:
        interval_options = request.query_params.get(
            'interval_options', IntervalOptions.ALL_TIME
        )
        sensor_process_service = SensorProcessService(
            sensor_repo=Sensor.objects,
        )
        process_data = sensor_process_service.get_process_data(
            interval_options=interval_options
        )

        return Response(
            process_data.model_dump(mode='json'),
            status=status.HTTP_200_OK,
        )


class SensorAggregatedApiView(APIView):
    permission_classes = (ApiKeyPermission,)

    def get(self, request: Request) -> Response:
        interval_options = request.query_params.get(
            'interval_options', IntervalOptions.ALL_TIME
        )

        sensor_column = Sensor.objects.find_many_by_columns(
            interval_options=interval_options
        )

        serializer = SensorAggregatedSerializer(instance=sensor_column)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )
