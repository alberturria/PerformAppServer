from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.delete_suite_use_case import DeleteSuiteUseCase
from waves.use_cases.get_suite_use_case import GetSuiteUseCase


class SuitesView(APIView):
    def delete(self, request, user_id, suite_id):
        try:
            delete_suite_use_case = DeleteSuiteUseCase(user_id, suite_id)
            return delete_suite_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)

    def get(self, request, user_id, suite_id):
        try:
            get_suite_use_case = GetSuiteUseCase(user_id, suite_id)
            return get_suite_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)
