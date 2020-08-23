from waves.entities.diagnosis_entity import DiagnosisEntity
from waves.interfaces.repositories.get_diagnosis_data_access_interface import GetDiagnosisDataAccessInterface
from waves.models import Diagnosis


class GetDiagnosisDataAccess(GetDiagnosisDataAccessInterface):

    def __init__(self, user_id, diagnosis_id):
        self._user_id = user_id
        self._diagnosis_id = diagnosis_id

    def get_diagnosis(self):
        diagnosis = Diagnosis.objects.get(id=self._diagnosis_id, owner__id=self._user_id)
        diagnosis_entity = DiagnosisEntity(diagnosis.id, diagnosis.name, diagnosis.description, diagnosis.video.url,
                                           diagnosis.owner_id, diagnosis.suite_id)
        return diagnosis_entity
