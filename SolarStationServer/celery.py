import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SolarStationServer.settings')

app = Celery('SolarStationServer')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'log_battery_voltage_every_hour': {
        'task': 'SolarStationServer.tasks.update_battery_voltage',
        'schedule': crontab(minute=0, hour='*'),
    },
}
app.conf.timezone = 'Europe/Kyiv'