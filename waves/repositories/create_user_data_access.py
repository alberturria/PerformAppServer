from django.contrib.auth.models import User
from waves.interfaces.repositories.create_user_data_access_interface import CreateUserDataAccessInterface
from rest_framework.authtoken.models import Token


class CreateUserDataAccess(CreateUserDataAccessInterface):
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def create_user(self):
        user = User.objects.create_user(
            username=self._username,
            password=self._password,
            email=self._email
        )
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        return {'user_id': user.id, 'username': user.username, 'token': token.key}
