from django.contrib.auth.models import User
from waves.entities.diagnosis_entity import DiagnosisEntity
from waves.entities.patient_entity import PatientEntity
from waves.interfaces.repositories.edit_patient_data_access_interface import EditPatientDataAccessInterface
from waves.models import Diagnosis, Suite, Patient
from waves.repositories.get_suite_data_access import GetSuiteDataAccess


class EditPatientDataAccess(EditPatientDataAccessInterface):

    def __init__(self, user_id, patient_entity):
        self._user_id = user_id
        self._patient_entity = patient_entity

    def edit_patient(self):
        patient = Patient.objects.get(id=self._patient_entity.id, owner__id=self._user_id)

        owner = User.objects.get(id=self._patient_entity.owner_id)
        patient.name = self._patient_entity.name
        patient.gender = self._patient_entity.gender
        patient.age = self._patient_entity.age
        patient.phone_number = self._patient_entity.phone_number
        patient.photo = self._patient_entity.photo
        patient.owner = owner

        patient.save()

        patient_entity = PatientEntity(patient.id, patient.name, patient.mail, patient.gender, patient.age,
                                       patient.phone_number, patient.photo.url, patient.owner.id)
        return patient_entity

    def get_related_suites(self):
        suites_id = Suite.objects.filter(patient__id=self._patient_entity.id).values_list('id', flat=True)
        suites_entities = []
        for suite_id in suites_id:
            suite_data_access = GetSuiteDataAccess(self._user_id, suite_id)

            suites_entities.append(suite_data_access.get_suite())

        return suites_entities
