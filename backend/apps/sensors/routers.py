from django.urls import path

from apps.sensors.views import SensorDataApiView, SensorProcessApiView


urlpatterns = [
    path('sensors/data', SensorDataApiView.as_view(), name='sensors_data'),
    path(
        'sensors/processed',
        SensorProcessApiView.as_view(),
        name='sensors_processed',
    ),
]
