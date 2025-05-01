from typing import Any

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Playground command for DEBUG and Testing'

    def handle(self, *args: Any, **options: Any) -> None:
        # sensor_process_service = SensorProcessService(
        #     sensor_repo=Sensor.objects,
        # )
        # iqr = sensor_process_service._get_iqr(
        #     values=[42, 58, 63, 77, 85, 240]
        # )
        print('Done')
