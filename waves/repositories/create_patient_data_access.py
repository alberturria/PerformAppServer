from django.contrib.auth.models import User
from waves.interfaces.repositories.create_patient_data_access_interface import CreatePatientDataAccessInterface
from waves.models import Patient


class CreatePatientDataAccess(CreatePatientDataAccessInterface):
    def __init__(self, user_id, patient_entity):
        self._user_id = user_id
        self._patient_entity = patient_entity

    def create_patient(self):
        owner = User.objects.get(id=self._patient_entity.owner_id)
        patient = Patient(name=self._patient_entity.name, mail=self._patient_entity.mail,
                          gender=self._patient_entity.gender, age=self._patient_entity.age,
                          phone_number=self._patient_entity.phone_number, photo=self._patient_entity.photo,
                          owner=owner)
        patient.save()
        return patient.id
