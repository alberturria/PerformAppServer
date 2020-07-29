from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.delete_patient_use_case import DeletePatientUseCase
from waves.use_cases.get_patient_use_case import GetPatientUseCase


class PatientView(APIView):
    def delete(self, request, user_id, patient_id):
        try:
            delete_patient_use_case = DeletePatientUseCase(user_id, patient_id)
            return delete_patient_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def get(self, request, user_id, patient_id):
        try:
            get_patient_use_case = GetPatientUseCase(user_id, patient_id)
            return get_patient_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)
