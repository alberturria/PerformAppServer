from rest_framework.response import Response
from waves.interfaces.use_cases.get_all_patients_use_case_interface import GetAllPatientsUseCaseInterface
from waves.repositories.get_all_patients_data_access import GetAllPatientsDataAccess


class GetAllPatientsUseCase(GetAllPatientsUseCaseInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def run(self):
        get_all_patients_data_access = GetAllPatientsDataAccess(self._user_id)
        patients_entities = get_all_patients_data_access.get_patients()
        parsed_patients = {}
        index = 0
        for patient in patients_entities:
            parsed_patients[index] = patient.__dict__
            index += 1
        return Response(data=parsed_patients, status=Response.status_code)
