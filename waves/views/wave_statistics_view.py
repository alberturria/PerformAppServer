
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.get_wave_statistics_use_case import GetWaveStatisticsUseCase


class WaveStatisticsView(APIView):
    def get(self, request, user_id, suite_id):
        try:
            get_wave_statistics_use_case = GetWaveStatisticsUseCase(user_id, suite_id)
            get_wave_statistics_use_case.run()
            return get_wave_statistics_use_case.get_response()

        except Exception as exception:
            return Response(data='Error', status=500)
