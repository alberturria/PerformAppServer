from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.create_sample_diagnoses_use_case import CreateSampleDiagnosesUseCase


class DiagnosesSampleDataView(APIView):

    def post(self, request, user_id):
        try:
            create_sample_diagnoses_use_case = CreateSampleDiagnosesUseCase(user_id)
            return create_sample_diagnoses_use_case.run()

        except Exception as exception:
            return Response(data=exception.args[0], status=500)
