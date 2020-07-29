from waves.entities.patient_entity import PatientEntity
from waves.interfaces.repositories.get_all_patients_data_access_interface import GetAllPatientsDataAccessInterface
from waves.models import Patient


class GetAllPatientsDataAccess(GetAllPatientsDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def get_patients(self):
        patients = Patient.objects.filter(owner__id=self._user_id)
        result = []

        for patient in patients:
            patient_entity = PatientEntity(patient.id, patient.name, patient.mail, patient.gender, patient.age,
                                           patient.phone_number, patient.photo.url, patient.owner.id)
            result.append(patient_entity)

        return result
