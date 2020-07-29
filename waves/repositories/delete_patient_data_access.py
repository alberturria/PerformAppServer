from waves.interfaces.repositories.delete_patient_data_access_interface import DeletePatientDataAccessInterface
from waves.models import Patient


class DeletePatientDataAccess(DeletePatientDataAccessInterface):
    def __init__(self, user_id, patient_id):
        self._user_id = user_id
        self._patient_id = patient_id

    def delete(self):
        suite = Patient.objects.get(id=self._patient_id, owner__id=self._user_id)
        suite.delete()
