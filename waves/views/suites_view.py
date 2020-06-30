from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.delete_suite_use_case import DeleteSuiteUseCase


class SuitesView(APIView):
    def delete(self, request, user_id, suite_id):
        try:
            delete_suite_use_case = DeleteSuiteUseCase(user_id, suite_id)
            return delete_suite_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)
