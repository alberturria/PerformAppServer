from rest_framework.response import Response
from waves.interfaces.use_cases.delete_diagnosis_use_case_interface import DeleteDiagnosisUseCaseInterface
from waves.repositories.delete_diagnosis_data_access import DeleteDiagnosisDataAccess


class DeleteDiagnosisUseCase(DeleteDiagnosisUseCaseInterface):
    def __init__(self, user_id, diagnosis_id):
        self._user_id = user_id
        self._diagnosis_id = diagnosis_id

    def run(self):
        delete_diagnosis_data_access = DeleteDiagnosisDataAccess(self._user_id, self._diagnosis_id)
        delete_diagnosis_data_access.delete()
        return Response(data=self._diagnosis_id, status=Response.status_code)
