from rest_framework.response import Response
from waves.interfaces.use_cases.edit_patient_use_case_interface import EditPatientUseCaseInterface
from waves.repositories.edit_patient_data_access import EditPatientDataAccess
from waves.repositories.get_patient_data_access import GetPatientDataAccess


class EditPatientUseCase(EditPatientUseCaseInterface):
    def __init__(self, user_id, patient_entity):
        self._user_id = user_id
        self._patient_entity = patient_entity

    def run(self):
        edit_patient_data_access = EditPatientDataAccess(self._user_id, self._patient_entity)
        patient = edit_patient_data_access.edit_patient()
        patient_data_access = GetPatientDataAccess(self._user_id, self._patient_entity.id)
        suites = patient_data_access.get_related_suites()
        result = {}
        index = 0
        result['patient'] = patient.__dict__
        result['suites'] = {}
        for suite in suites:
            result['suite'][index] = suite.__dict__
            index += 1

        return Response(data=result, status=Response.status_code)
