from waves.entities.patient_entity import PatientEntity
from waves.interfaces.repositories.get_patient_data_access_interface import GetPatientDataAccessInterface
from waves.models import Suite, Patient
from waves.repositories.get_suite_data_access import GetSuiteDataAccess


class GetPatientDataAccess(GetPatientDataAccessInterface):

    def __init__(self, user_id, patient_id):
        self._user_id = user_id
        self._patient_id = patient_id

    def get_patient(self):
        patient = Patient.objects.get(id=self._patient_id, owner__id=self._user_id)
        patient_entity = PatientEntity(patient.id, patient.name, patient.mail, patient.gender, patient.age,
                                       patient.phone_number, patient.photo.url, patient.owner.id)
        return patient_entity

    def get_related_suites(self):

        suites_id = Suite.objects.filter(patient__id=self._patient_id).values_list('id', flat=True)
        suites_entities = []
        for suite_id in suites_id:
            suite_data_access = GetSuiteDataAccess(self._user_id, suite_id)
    
            suites_entities.append(suite_data_access.get_suite())

        return suites_entities
