from celery import Celery
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
django.setup()
app = Celery("djangoapp", broker='amqp://guest:guest@localhost:5672//')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
