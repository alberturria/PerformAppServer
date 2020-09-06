from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from waves.use_cases.get_fatigue_analysis_use_case import GetFatigueAnalysisUseCase


class FatigueAnalysisView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id, suite_id):
        try:
            if request.auth.user_id is not int(user_id):
                raise Exception
            get_fatigue_use_case = GetFatigueAnalysisUseCase(user_id, suite_id)
            return get_fatigue_use_case.run()

        except Exception as exception:
            return Response(data='Error', status=500)
