from django.contrib.auth.models import User
from waves.interfaces.repositories.create_diagnosis_data_access_interface import CreateDiagnosisDataAccessInterface
from waves.interfaces.repositories.create_patient_data_access_interface import CreatePatientDataAccessInterface
from waves.models import Patient, Diagnosis, Suite


class CreateDiagnosisDataAccess(CreateDiagnosisDataAccessInterface):
    def __init__(self, user_id, diagnosis_entity):
        self._user_id = user_id
        self._diagnosis_entity = diagnosis_entity

    def create_diagnosis(self):
        owner = User.objects.get(id=self._diagnosis_entity.owner_id)
        suite = None
        if self._diagnosis_entity.suite_id:
            suite = Suite.objects.get(id=self._diagnosis_entity.suite_id)

        diagnosis = Diagnosis(name= self._diagnosis_entity.name, description=self._diagnosis_entity.description,
                              video=self._diagnosis_entity.video, suite=suite, owner=owner)
        diagnosis.save()
        return diagnosis.id
