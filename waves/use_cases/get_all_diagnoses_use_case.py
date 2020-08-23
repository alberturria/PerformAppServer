from rest_framework.response import Response
from waves.interfaces.use_cases.get_all_diagnoses_use_case_interface import GetAllDiagnosesUseCaseInterface
from waves.repositories.get_all_diagnoses_data_access import GetAllDiagnosesDataAccess


class GetAllDiagnosesUseCase(GetAllDiagnosesUseCaseInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def run(self):
        get_all_diagnoses_data_access = GetAllDiagnosesDataAccess(self._user_id)
        diagnoses_entities = get_all_diagnoses_data_access.get_diagnoses()
        parsed_diagnoses = {}
        index = 0
        for diagnosis in diagnoses_entities:
            parsed_diagnoses[index] = diagnosis.__dict__
            index += 1
        return Response(data=parsed_diagnoses, status=Response.status_code)
