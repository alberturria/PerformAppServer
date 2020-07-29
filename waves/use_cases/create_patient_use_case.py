from rest_framework.response import Response
from waves.interfaces.use_cases.create_patient_use_case_interface import CreatePatientUseCaseInterface
from waves.interfaces.use_cases.create_user_use_case_interface import CreateUserUseCaseInterface
from waves.repositories.create_patient_data_access import CreatePatientDataAccess
from waves.repositories.create_user_data_access import CreateUserDataAccess


class CreatePatientUseCase(CreatePatientUseCaseInterface):
    def __init__(self, user_id, patient_entity):
        self._user_id = user_id
        self._patient_entity = patient_entity

    def run(self):
        create_patient_data_access = CreatePatientDataAccess(self._user_id, self._patient_entity)
        patient_id = create_patient_data_access.create_patient()
        return Response(data=patient_id, status=Response.status_code)
