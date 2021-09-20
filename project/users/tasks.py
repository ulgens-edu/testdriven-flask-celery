import time

from celery import shared_task


@shared_task
def divide(x, y):
    time.sleep(5)
    return x / y
