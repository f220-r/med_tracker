from django.contrib.auth.backends import BaseBackend
from preview.models import User

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            else:
                aux_user = user
                aux_user.password = None
                # If the password doesn't match, return the email
                return aux_user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
