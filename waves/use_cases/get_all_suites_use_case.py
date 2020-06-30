from rest_framework.response import Response
from waves.interfaces.use_cases.get_all_suites_use_case_interface import GetAllSuitesUseCaseInterface
from waves.repositories.get_all_suites_data_access import GetAllSuitesDataAccess


class GetAllSuitesUseCase(GetAllSuitesUseCaseInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def run(self):
        get_all_suites_data_access = GetAllSuitesDataAccess(self._user_id)
        suites_entities = get_all_suites_data_access.get_suites()
        parsed_suites = {}
        index = 0
        for suites in suites_entities:
            parsed_suites[index] = suites.__dict__
            index += 1
        return Response(data=parsed_suites, status=Response.status_code)
