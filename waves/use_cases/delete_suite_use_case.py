from rest_framework.response import Response
from waves.interfaces.use_cases.delete_suite_use_case_interface import DeleteSuiteUseCaseInterface
from waves.repositories.delete_suite_data_access import DeleteSuiteDataAccess


class DeleteSuiteUseCase(DeleteSuiteUseCaseInterface):
    def __init__(self, user_id, suite_id):
        self._user_id = user_id
        self._suite_id = suite_id

    def run(self):
        delete_suite_data_access = DeleteSuiteDataAccess(self._user_id, self._suite_id)
        delete_suite_data_access.delete()
        return Response(data=self._suite_id, status=Response.status_code)
