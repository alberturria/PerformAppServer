from rest_framework.response import Response
from waves.interfaces.use_cases.log_user_use_case_interface import LogUserUseCaseInterface
from waves.repositories.log_user_data_access import LogUserDataAccess


class LogUserUseCase(LogUserUseCaseInterface):
    def __init__(self, email, password):
        self._email = email
        self._password = password

    def run(self):
        log_user_data_access = LogUserDataAccess(self._email, self._password)
        user_data = log_user_data_access.log_user()
        return Response(data=user_data, status=Response.status_code)
