from rest_framework.response import Response
from waves.interfaces.use_cases.create_sample_patients_use_case_interface import CreateSamplePatientsUseCaseInterface
from waves.repositories.create_sample_patients_data_access import CreateSamplePatientsDataAccess


class CreateSamplePatientsUseCase(CreateSamplePatientsUseCaseInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def run(self):
        create_sample_data_data_access = CreateSamplePatientsDataAccess(self._user_id)
        patients_entities = create_sample_data_data_access.create_sample_patients()
        parsed_patients = {}
        index = 0
        for patient in patients_entities:
            parsed_patients[index] = patient.__dict__
            index += 1
        return Response(data=parsed_patients, status=Response.status_code)
