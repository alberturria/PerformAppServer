from rest_framework.response import Response
from waves.interfaces.use_cases.delete_patient_use_case_interface import DeletePatientUseCaseInterface
from waves.repositories.delete_patient_data_access import DeletePatientDataAccess


class DeletePatientUseCase(DeletePatientUseCaseInterface):
    def __init__(self, user_id, patient_id):
        self._user_id = user_id
        self._patient_id = patient_id

    def run(self):
        delete_patient_data_access = DeletePatientDataAccess(self._user_id, self._patient_id)
        delete_patient_data_access.delete()
        return Response(data=self._patient_id, status=Response.status_code)
