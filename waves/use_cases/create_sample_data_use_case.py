from rest_framework.response import Response
from waves.interfaces.use_cases.create_sample_data_use_case_interface import CreateSampleDataUseCaseInterface
from waves.repositories.create_sample_data_data_access import CreateSampleDataDataAccess


class CreateSampleDataUseCase(CreateSampleDataUseCaseInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def run(self):
        create_sample_data_data_access = CreateSampleDataDataAccess(self._user_id)
        create_sample_data_data_access.create_sample_data()
        return Response(status=Response.status_code)
