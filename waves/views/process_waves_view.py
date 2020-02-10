from common.utils.read_csv import read_csv_file
from rest_framework.response import Response
from rest_framework.views import APIView
from waves.use_cases.draw_rms_use_case import DrawRMSUseCase
from waves.use_cases.draw_wave_use_case import DrawWaveUseCase
from waves.use_cases.get_fft_use_case import GetFFTUSeCase
from waves.use_cases.get_mdf_use_case import GetMDFUseCase
from waves.use_cases.get_mnf_use_case import GetMNFUseCase


class ProcessWavesView(APIView):

    def get(self, request):
        try:
            read_csv_file('./data/basic_mdurance_1.csv')
            draw_rms_use_case = DrawRMSUseCase(19)
            #draw_rms_use_case.run()

            get_fft_use_case = GetFFTUSeCase(19)
            get_fft_use_case.run()
            fft_wave = get_fft_use_case.get_result()

            draw_wave_use_case = DrawWaveUseCase(fft_wave)
            #draw_wave_use_case.run()

            #get_mdf_use_case = GetMDFUseCase(fft_wave)
            #get_mdf_use_case.run()
            #mdf_wave = get_mdf_use_case.get_result()

            #draw_wave_use_case = DrawWaveUseCase(mdf_wave)
            #draw_wave_use_case.run()

            get_mnf_use_case = GetMNFUseCase(fft_wave)
            get_mnf_use_case.run()
            mnf_wave = get_mnf_use_case.get_result()

            draw_wave_use_case = DrawWaveUseCase(mnf_wave)
            draw_wave_use_case.run()


            return Response(data=3, status=Response.status_code)

        except Exception as exception:
            print(exception)
