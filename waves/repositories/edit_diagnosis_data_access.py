from waves.entities.diagnosis_entity import DiagnosisEntity
from waves.interfaces.repositories.edit_diagnosis_data_access_interface import EditDiagnosisDataAccessInterface
from waves.models import Diagnosis, Suite


class EditDiagnosisDataAccess(EditDiagnosisDataAccessInterface):

    def __init__(self, user_id, diagnosis_entity):
        self._user_id = user_id
        self._diagnosis_entity = diagnosis_entity

    def edit_diagnosis(self):
        diagnosis = Diagnosis.objects.get(id=self._diagnosis_entity.id, owner__id=self._user_id)
        suite = None
        if self._diagnosis_entity.suite_id:
            suite = Suite.objects.get(id=self._diagnosis_entity.suite_id)
        diagnosis.name = self._diagnosis_entity.name
        diagnosis.description = self._diagnosis_entity.description
        diagnosis.video = self._diagnosis_entity.video
        diagnosis.suite = suite
        diagnosis.save()
        diagnosis_entity = DiagnosisEntity(diagnosis.id, diagnosis.name, diagnosis.description, diagnosis.video.url,
                                           diagnosis.owner_id, diagnosis.suite_id)
        return diagnosis_entity
