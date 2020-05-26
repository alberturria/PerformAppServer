import json

from common.utils.convert_to_dictionary import ConvertToDictionary
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.repositories.get_wave_data_access import GetWaveDataAccess
from waves.repositories.get_waves_data_access import GetWavesDataAccess
from waves.use_cases.get_sections_use_case import GetSectionsUseCase


class RmsSectionsView(APIView):

    def get(self, request, wave_id):
        try:
            get_wave_data_access = GetWaveDataAccess(wave_id)
            wave_entity = get_wave_data_access.get_wave()
            get_sections_use_case = GetSectionsUseCase(wave_entity=wave_entity)
            get_sections_use_case.run()
            rms_sections = get_sections_use_case.get_rms_sections()
            parsed_rms_sections = {}
            index = 0
            for rms_section in rms_sections:
                parsed_rms_sections[index] = rms_section.__dict__
                index += 1
            return Response(data=parsed_rms_sections, status=Response.status_code)

        except Exception as exception:
            print(exception)
