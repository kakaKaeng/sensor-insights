from django.urls import path

from apps.sensors.views import SensorsDataApiView

urlpatterns = [
    path('sensors/data', SensorsDataApiView.as_view(), name='sensors-data'),
]
