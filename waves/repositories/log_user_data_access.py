from django.contrib.auth.models import User
from waves.interfaces.repositories.log_user_data_access_interface import LogUserDataAccessInterface
from rest_framework.authtoken.models import Token


class LogUserDataAccess(LogUserDataAccessInterface):
    def __init__(self, email, password):
        self._email = email
        self._password = password

    def log_user(self):
        user = User.objects.get(email=self._email)
        if user.check_password(self._password):
            token, created = Token.objects.get_or_create(user=user)
            return {'user_id': user.id, 'username': user.username, 'token': token.key}
        else:
            return Exception
