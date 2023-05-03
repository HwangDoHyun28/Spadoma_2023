from celery import Celery
import os

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_DB = os.environ['POSTGRES_DB']
REDIS_HOST = os.environ['REDIS_HOST']

celery_task = Celery(
    'app',
    broker=f"redis://{REDIS_HOST}:6379/0",
    backend=f"db+postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}",
    include=['app.celery_worker']
)
