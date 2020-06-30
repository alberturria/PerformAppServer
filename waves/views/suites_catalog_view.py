from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.get_all_suites_use_case import GetAllSuitesUseCase
from waves.use_cases.log_user_use_case import LogUserUseCase


class SuitesCatalogView(APIView):
    def get(self, request, user_id):
        try:
            get_all_sections_use_case = GetAllSuitesUseCase(user_id)
            return get_all_sections_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)
