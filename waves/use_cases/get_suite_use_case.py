from rest_framework.response import Response
from waves.interfaces.use_cases.get_suite_use_case_interface import GetSuiteUseCaseInterface
from waves.repositories.get_suite_data_access import GetSuiteDataAccess


class GetSuiteUseCase(GetSuiteUseCaseInterface):
    def __init__(self, user_id, suite_id):
        self._user_id = user_id
        self._suite_id = suite_id

    def run(self):
        suite_data_access = GetSuiteDataAccess(self._user_id, self._suite_id)
        suite = suite_data_access.get_suite()
        waves = suite_data_access.get_waves()
        result = {}
        index = 0

        result['suite'] = suite.__dict__
        result['waves'] = {}
        for wave in waves:
            result['waves'][index] = wave.__dict__
            index += 1

        return Response(data=result, status=Response.status_code)

