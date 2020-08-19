from rest_framework.response import Response
from waves.interfaces.use_cases.create_diagnosis_use_case_interface import CreateDiagnosisUseCaseInterface
from waves.repositories.create_diagnosis_data_access import CreateDiagnosisDataAccess


class CreateDiagnosisUseCase(CreateDiagnosisUseCaseInterface):
    def __init__(self, user_id, diagnosis_entity):
        self._user_id = user_id
        self._diagnosis_entity = diagnosis_entity

    def run(self):
        create_diagnosis_data_access = CreateDiagnosisDataAccess(self._user_id, self._diagnosis_entity)
        diagnosis_id = create_diagnosis_data_access.create_diagnosis()
        return Response(data=diagnosis_id, status=Response.status_code)
