from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.create_sample_data_use_case import CreateSampleDataUseCase


class CreateSampleDataView(APIView):

    def post(self, request, user_id):
        try:
            log_user_use_case = CreateSampleDataUseCase(user_id)
            return log_user_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=403)
