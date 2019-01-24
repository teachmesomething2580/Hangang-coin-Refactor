from celery import Celery
from django.conf import settings


if settings.DEBUG is True:
    url = 'localhost'
else:
    url = 'hangang-coin-redis.ke2lqx.0001.apn2.cache.amazonaws.com'

app = Celery('tasks',
             broker='redis://'+url+':6379/0',
             backend='redis://'+url+':6379/0'
             )

app.conf.beat_schedule = {
    'crawling-coin-every-1-min': {
        'task': 'coin.tasks.get_all_coin_with_celery',
        'schedule': 60.0,
    },
    'crawling-river-every-30-min': {
        'task': 'river.tasks.get_river_temperature_with_celery',
        'schedule': 180.0,
    },
}

app.autodiscover_tasks()
