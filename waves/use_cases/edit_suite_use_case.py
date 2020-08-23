from rest_framework.response import Response
from waves.interfaces.use_cases.edit_suite_use_case_interface import EditSuiteUseCaseInterface
from waves.repositories.edit_suite_data_access import EditSuiteDataAccess


class EditSuiteUseCase(EditSuiteUseCaseInterface):
    def __init__(self, user_id, suite_entity):
        self._user_id = user_id
        self._suite_entity = suite_entity

    def run(self):
        edit_suite_data_access = EditSuiteDataAccess(self._user_id, self._suite_entity)
        suite_id = edit_suite_data_access.edit_suite()

        return Response(data=suite_id, status=Response.status_code)
