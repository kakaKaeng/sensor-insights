from django.urls import path

from apps.sensors.views import SensorsView

urlpatterns = [
    path('sensors/data', SensorsView.as_view(), name='sensors'),
]
