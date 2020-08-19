from rest_framework.response import Response
from waves.interfaces.use_cases.edit_diagnosis_use_case_interface import EditDiagnosisUseCaseInterface
from waves.repositories.edit_diagnosis_data_access import EditDiagnosisDataAccess


class EditDiagnosisUseCase(EditDiagnosisUseCaseInterface):
    def __init__(self, user_id, diagnosis_entity):
        self._user_id = user_id
        self._diagnosis_entity = diagnosis_entity

    def run(self):
        edit_diagnosis_data_access = EditDiagnosisDataAccess(self._user_id, self._diagnosis_entity)
        diagnosis = edit_diagnosis_data_access.edit_diagnosis()
        result = {}
        result['diagnosis'] = diagnosis.__dict__

        return Response(data=result, status=Response.status_code)
