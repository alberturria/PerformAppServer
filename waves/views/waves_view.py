import json

from common.utils.convert_to_dictionary import ConvertToDictionary
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.repositories.get_waves_data_access import GetWavesDataAccess


class WavesView(APIView):

    def get(self, request):
        try:
            get_waves_data_access = GetWavesDataAccess()
            waves = get_waves_data_access.get_waves()
            parsed_waves = {}
            index = 0
            for wave in waves:
                parsed_waves[index] = wave.__dict__
                index += 1
            return Response(data=parsed_waves, status=Response.status_code)

        except Exception as exception:
            print(exception)
