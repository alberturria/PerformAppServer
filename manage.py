#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django
from waves.use_cases.compare_all_rms_per_sections_use_case import CompareAllRMSPerSectionsUseCase
from waves.use_cases.get_sections_use_case import GetSectionsUseCase

django.setup()

from common.utils.read_csv import read_csv_file
from waves.repositories.get_waves_data_access import GetWavesDataAccess
from waves.use_cases.draw_wave_use_case import DrawWaveUseCase
from waves.use_cases.get_fft_use_case import GetFFTUSeCase
from waves.use_cases.get_mnf_use_case import GetMNFUseCase
from sklearn.cluster import KMeans


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
    try:
        from django.core.management import execute_from_command_line

        #read_csv_file('./data/basic_mdurance_1.csv')
        #get_wave_data_access = GetWavesDataAccess()
        #waves = get_wave_data_access.get_waves()

        #compare_use_case = CompareAllRMSPerSectionsUseCase(waves)
        #compare_use_case.run()
        #comparison = compare_use_case.get_result()

        #get_sections_use_case = GetSectionsUseCase(waves[0])
        #get_sections_use_case.run()
        #rms_sections = get_sections_use_case.get_rms_sections()
        #raw_sections = get_sections_use_case.get_raw_sections()

        #get_fft_use_case = GetFFTUSeCase(19)
        #get_fft_use_case.run()
        #fft_wave = get_fft_use_case.get_result()

        #draw_wave_use_case = DrawWaveUseCase(fft_wave)
        ## draw_wave_use_case.run()

        ## get_mdf_use_case = GetMDFUseCase(fft_wave)
        ## get_mdf_use_case.run()
        ## mdf_wave = get_mdf_use_case.get_result()

        ## draw_wave_use_case = DrawWaveUseCase(mdf_wave)
        ## draw_wave_use_case.run()

        #get_mnf_use_case = GetMNFUseCase(fft_wave)
        #get_mnf_use_case.run()
        #mnf_wave = get_mnf_use_case.get_result()

        #draw_wave_use_case = DrawWaveUseCase(mnf_wave)
        ##draw_wave_use_case.run()



    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
