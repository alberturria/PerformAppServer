from rest_framework.response import Response
from waves.interfaces.use_cases.create_sample_diagnoses_use_case_interface import CreateSampleDiagnosesUseCaseInterface
from waves.repositories.create_sample_diagnoses_data_access import CreateSampleDiagnosesDataAccess


class CreateSampleDiagnosesUseCase(CreateSampleDiagnosesUseCaseInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def run(self):
        create_sample_diagnoses_data_access = CreateSampleDiagnosesDataAccess(self._user_id)
        diagnoses_entities = create_sample_diagnoses_data_access.create_sample_diagnoses()
        parsed_diagnoses = {}
        index = 0
        for diagnosis in diagnoses_entities:
            parsed_diagnoses[index] = diagnosis.__dict__
            index += 1
        return Response(data=parsed_diagnoses, status=Response.status_code)
