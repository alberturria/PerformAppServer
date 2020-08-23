from django.contrib.auth.models import User
from waves.entities.diagnosis_entity import DiagnosisEntity
from waves.interfaces.repositories.create_sample_diagnoses_data_access_interface import \
    CreateSampleDiagnosesDataAccessInterface
from waves.models import Diagnosis


class CreateSampleDiagnosesDataAccess(CreateSampleDiagnosesDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def create_sample_diagnoses(self):
        owner = User.objects.get(id=self._user_id)

        diagnosis1 = Diagnosis(name='Diagnóstico 1',
                               description='El deportista, como se puede apreciar en la prueba realizada, no logra '
                                           'obtener una simetría muscular, por lo que se recomienda que trabaje cada '
                                           'grupo muscular de manera aislada.',
                               owner=owner)
        diagnosis2 = Diagnosis(name='Diagnóstico 2',
                               description='El paciente parece haber sufrido una lesión postural. El músculo piramidal '
                                           ' ha presentado una alta actrividad durante toda la prueba, pese a no ser'
                                           ' requerida ninguna actividad.',
                               owner=owner)
        diagnosis1.save()
        diagnosis2.save()

        diagnoses = Diagnosis.objects.filter(owner__id=self._user_id)
        result = []

        for diagnosis in diagnoses:
            diagnosis_entity = DiagnosisEntity(diagnosis.id, diagnosis.name, diagnosis.description, diagnosis.video.url,
                                               diagnosis.owner.id, diagnosis.suite_id)
            result.append(diagnosis_entity)

        return result
