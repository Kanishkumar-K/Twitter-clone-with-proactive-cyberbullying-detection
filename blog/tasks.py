# tasks.py

from celery import shared_task
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

@shared_task
def reactivate_inactive_users():
    # Get inactive users whose last deactivation was more than 1 minute ago
    inactive_users = User.objects.filter(is_active=False, profile__last_deactivated__lte=timezone.now() - timedelta(minutes=1))
    for user in inactive_users:
        # Reactivate the user by setting is_active to True
        user.is_active = True
        user.save()
