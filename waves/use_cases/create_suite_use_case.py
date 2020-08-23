from rest_framework.response import Response
from waves.interfaces.use_cases.create_suite_use_case_interface import CreateSuiteUseCaseInterface
from waves.repositories.create_suite_data_access import CreateSuiteDataAccess


class CreateSuiteUseCase(CreateSuiteUseCaseInterface):
    def __init__(self, user_id, suite_entity):
        self._user_id = user_id
        self.suite_entity = suite_entity

    def run(self):
        create_suite_data_access = CreateSuiteDataAccess(self._user_id, self.suite_entity)
        suite_id = create_suite_data_access.create_suite()
        return Response(data=suite_id, status=Response.status_code)
