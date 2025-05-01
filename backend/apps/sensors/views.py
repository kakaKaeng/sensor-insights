from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class SensorsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request) -> Response:
        data = {'message': 'Hello, world!'}
        return Response(data, status=status.HTTP_200_OK)


class SensorsDataApiView(APIView):
    permission_classes = (AllowAny,)
