from django.urls import path

from apps.sensors.views import (
    SensorDataApiView,
    SensorProcessedApiView,
    SensorAggregatedApiView,
    TestApiView,
)

urlpatterns = [
    path('sensors/data', SensorDataApiView.as_view(), name='sensors_data'),
    path(
        'sensors/processed',
        SensorProcessedApiView.as_view(),
        name='sensors_processed',
    ),
    path(
        'sensors/aggregated',
        SensorAggregatedApiView.as_view(),
        name='sensors_aggregated',
    ),
    path(
        'sensors/test',
        TestApiView.as_view(),
        name='sensors_test',
    )
]
