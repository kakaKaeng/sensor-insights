from typing import Any

from django.contrib import admin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

from apps.sensors.forms import CSVUploadForm
from apps.sensors.models import Sensor
from apps.sensors.services.sensor_csv import SensorCSVService


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):  # type: ignore
    model = Sensor
    list_display = ('id', 'timestamp', 'temperature', 'humidity', 'air_quality')
    change_list_template = 'sensor_change_list.html'

    def get_urls(self) -> Any:
        urls = super().get_urls()

        return urls + [
            path(
                'import-csv',
                self.admin_site.admin_view(SensorCSVImportView.as_view()),
                name='sensors_import_csv',
            )
        ]


class SensorCSVImportView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request: HttpRequest) -> HttpResponse:
        form = CSVUploadForm()
        return render(request, 'csv_import.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponseRedirect | HttpResponse:
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            sensor_csv_service = SensorCSVService()
            sensor_csv_service.import_csv(csv_file=csv_file)
        else:
            return render(request, 'csv_import.html', {'form': form})
        return HttpResponseRedirect(reverse('admin:sensors_sensor_changelist'))
