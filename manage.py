#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import django
from waves.use_cases.compare_all_rms_per_sections_use_case import CompareAllRMSPerSectionsUseCase
from waves.use_cases.get_data_range_use_case import GetDataRangeUseCase
from waves.use_cases.get_kurtosis_use_case import GetKurtosisUseCase
from waves.use_cases.get_sections_use_case import GetSectionsUseCase

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

django.setup()

import matplotlib.pyplot as plt

from waves.use_cases.get_maximum_use_case import GetMaximumUseCase
from waves.use_cases.get_means_use_case import GetMeansUseCase
from waves.use_cases.get_entropy_use_case import GetEntropyUseCase
from waves.use_cases.get_energy_use_case import GetEnergyUseCase
from common.utils.read_csv import read_csv_file
from waves.repositories.get_waves_data_access import GetWavesDataAccess
from waves.use_cases.draw_wave_use_case import DrawWaveUseCase
from waves.use_cases.get_fft_use_case import GetFFTUSeCase
from waves.use_cases.get_mnf_use_case import GetMNFUseCase
from sklearn.cluster import KMeans
from waves.use_cases.get_psdf_use_case import GetPSDFUseCase
from waves.use_cases.get_zero_crossing_counts_use_case import GetZeroCrossingCountsUseCase
from waves.use_cases.get_wavelet_use_case import GetWaveletUseCase




def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')
    try:
        from django.core.management import execute_from_command_line


#        read_csv_file('./data/basic_mdurance-test.csv')
    #    get_wave_data_access = GetWavesDataAccess()
    #    waves = get_wave_data_access.get_waves()

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

   #     get_mnf_use_case = GetMNFUseCase(waves[0]._raw)
    #    get_mnf_use_case.run()
     #   mnf_wave = get_mnf_use_case.get_result()

        #draw_wave_use_case = DrawWaveUseCase(mnf_wave)
        ##draw_wave_use_case.run()

        #get_energy_use_case = GetEnergyUseCase(19)
        #get_energy_use_case.run()
        #energy = get_energy_use_case.get_result()

        #get_entropy_use_case = GetEntropyUseCase(waves[0]._rms)
        #get_entropy_use_case.run()
        #entropy = get_entropy_use_case.get_result()

        #get_means_use_case = GetMeansUseCase(waves[0]._rms)
        #get_means_use_case.run()
        #means = get_means_use_case.get_result()

        #get_maximum_use_case = GetMaximumUseCase(waves[0]._rms)
        #get_maximum_use_case.run()
        #maximum_value_position_entity = get_maximum_use_case.get_result()

        #get_kurtosis_use_case = GetKurtosisUseCase(waves[0]._rms)
        #get_kurtosis_use_case.run()
        #kurtosis = get_kurtosis_use_case.get_result()

        #get_data_range_use_case = GetDataRangeUseCase(waves[0]._rms)
        #get_data_range_use_case.run()
        #range = get_data_range_use_case.get_result()

  #      get_zero_crossing_counts_use_case = GetZeroCrossingCountsUseCase(waves[0]._raw)
   #     get_zero_crossing_counts_use_case.run()
    #    zcc = get_zero_crossing_counts_use_case.get_result()

        #get_psdf_use_case = GetPSDFUseCase(waves[0]._raw)
        #get_psdf_use_case.run()
        #frequencies, psdf = get_psdf_use_case.get_result()

   #     get_wavelet_use_case = GetWaveletUseCase(waves[0]._raw)
    #    get_wavelet_use_case.run()


    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
