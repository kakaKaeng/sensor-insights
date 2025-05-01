from django.urls import path

from apps.sensors.views import SensorDataApiView

urlpatterns = [
    path('sensors/data', SensorDataApiView.as_view(), name='sensors_data'),
]
