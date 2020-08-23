from rest_framework.response import Response
from waves.interfaces.use_cases.get_patient_use_case_interface import GetPatientUseCaseInterface
from waves.repositories.get_patient_data_access import GetPatientDataAccess


class GetPatientUseCase(GetPatientUseCaseInterface):
    def __init__(self, user_id, patient_id):
        self._user_id = user_id
        self._patient_id = patient_id

    def run(self):
        suite_data_access = GetPatientDataAccess(self._user_id, self._patient_id)
        patient = suite_data_access.get_patient()
        suites = suite_data_access.get_related_suites()
        result = {}
        index = 0

        result['patient'] = patient.__dict__
        result['suites'] = {}
        for suite in suites:
            result['suites'][index] = suite.__dict__
            index += 1

        return Response(data=result, status=Response.status_code)

