from rest_framework.response import Response
from waves.interfaces.use_cases.create_user_use_case_interface import CreateUserUseCaseInterface
from waves.repositories.create_user_data_access import CreateUserDataAccess


class CreateUserUseCase(CreateUserUseCaseInterface):
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self._password = password

    def run(self):
        create_user_data_access = CreateUserDataAccess(self._username, self._email, self._password)
        user_id = create_user_data_access.create_user()
        return Response(data=user_id, status=Response.status_code)
