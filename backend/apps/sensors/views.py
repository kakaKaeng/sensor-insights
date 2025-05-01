from urllib.request import Request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.commons.permissions import ApiKeyPermission
from apps.sensors.serializers import SensorDataSerializer


class SensorsDataApiView(APIView):
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
