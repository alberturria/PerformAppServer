from waves.entities.diagnosis_entity import DiagnosisEntity
from waves.interfaces.repositories.get_all_diagnoses_data_access_interface import GetAllDiagnosesDataAccessInterface
from waves.models import Diagnosis


class GetAllDiagnosesDataAccess(GetAllDiagnosesDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def get_diagnoses(self):
        diagnoses = Diagnosis.objects.filter(owner__id=self._user_id)
        result = []

        for diagnosis in diagnoses:
            suite_name = diagnosis.suite.name if diagnosis.suite else None
            patient_name = diagnosis.suite.patient.name if diagnosis.suite and diagnosis.suite.patient else None

            diagnosis_entity = DiagnosisEntity(diagnosis.id, diagnosis.name, diagnosis.description, diagnosis.video.url,
                                               diagnosis.owner.id, diagnosis.suite_id, suite_name,
                                               patient_name)
            result.append(diagnosis_entity)

        return result
