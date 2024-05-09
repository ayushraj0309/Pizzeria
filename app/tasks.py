# tasks.py
from celery import shared_task
from datetime import datetime, timedelta
from .models import OrderTask, PizzaOrder


@shared_task
def update_order_status(order_id):
    order = PizzaOrder.objects.get(pk=order_id)
    now = datetime.now()
    tasks = [
        (now + timedelta(minutes=1), 'Accepted'),
        (now + timedelta(minutes=2), 'Preparing'),
        (now + timedelta(minutes=5), 'Dispatched'),
        (now + timedelta(minutes=10), 'Delivered'),
    ]

    for task_time, task_status in tasks:
        OrderTask.objects.create(pizza_order=order, task_time=task_time, task_status=task_status)
