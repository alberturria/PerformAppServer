from rest_framework.response import Response
from waves.interfaces.use_cases.get_diagnosis_use_case_interface import GetDiagnosisUseCaseInterface
from waves.repositories.get_diagnosis_data_access import GetDiagnosisDataAccess


class GetDiagnosisUseCase(GetDiagnosisUseCaseInterface):
    def __init__(self, user_id, diagnosis_id):
        self._user_id = user_id
        self._diagnosis_id = diagnosis_id

    def run(self):
        diagnosis_data_access = GetDiagnosisDataAccess(self._user_id, self._diagnosis_id)
        diagnosis = diagnosis_data_access.get_diagnosis()
        result = {}
        result['diagnosis'] = diagnosis.__dict__

        return Response(data=result, status=Response.status_code)
