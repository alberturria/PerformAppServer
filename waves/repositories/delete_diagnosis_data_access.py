from waves.interfaces.repositories.delete_diagnosis_data_access_interface import DeleteDiagnosisDataAccessInterface
from waves.models import Diagnosis


class DeleteDiagnosisDataAccess(DeleteDiagnosisDataAccessInterface):
    def __init__(self, user_id, diagnosis_id):
        self._user_id = user_id
        self._diagnosis_id = diagnosis_id

    def delete(self):
        diagnosis = Diagnosis.objects.get(id=self._diagnosis_id, owner__id=self._user_id)
        diagnosis.delete()
