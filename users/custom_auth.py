# custom_auth.py

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return

        # Check if the user is blocked
        if user.is_blocked_until is not None and user.is_blocked_until > timezone.now():
            # User is blocked, reject authentication
            return None

        # Check the password and return the user if authenticated
        if user.check_password(password):
            return user
        else:
            return None


