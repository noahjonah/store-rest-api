import os
from celery import Celery


# Setting an env variable to storefront settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings')

# Celery instance
celery = Celery('storefront')
# Celery can find configurations at -> django.conf loading settings module
celery.config_from_object('django.conf:settings', namespace='CELERY')

# celery tasks discovering automatically from task moduless
celery.autodiscover_tasks()
