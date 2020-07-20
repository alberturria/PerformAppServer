import csv
import pandas as pd
from django.contrib.auth.models import User

from waves.models import Wave, Suite


def read_csv_file(file_path, second_file_path, user_id=None):
    numbers_of_suites = 4
    csv_file = pd.read_csv(file_path, sep=';')
    headers = csv_file.columns
    names = csv_file[headers[0]]
    avg_rms = csv_file[headers[1]]
    rms_per_seconds = csv_file[headers[2]]
    mvcs = csv_file[headers[3]]
    historic_mvcs = csv_file[headers[4]]

    csv_file = pd.read_csv(file_path, sep=';')
    headers = csv_file.columns
    names = csv_file[headers[0]]
    avg_rmss = csv_file[headers[1]]
    rms_per_seconds = csv_file[headers[2]]
    mvcs = csv_file[headers[3]]
    historic_mvcs = csv_file[headers[4]]

    csv_file_2 = pd.read_csv(second_file_path, sep=';')

    raw_1 = csv_file_2['emg_muscle_1_(µV)'].to_list()
    raw_2 = csv_file_2['emg_muscle_2_(µV)'].to_list()
    raw_3 = csv_file_2['emg_muscle_3_(µV)'].to_list()
    raw_4 = csv_file_2['emg_muscle_4_(µV)'].to_list()
    total_raw = [raw_1, raw_2, raw_3, raw_4]

    frames = csv_file['frames_(0.25s)']
    column_1 = csv_file['rms_1_(µV)']
    column_2 = csv_file['rms_2_(µV)']
    column_3 = csv_file['rms_3_(µV)']
    column_4 = csv_file['rms_4_(µV)']
    frames = csv_file['frames_(0.25s)'].to_list()
    rms_1 = csv_file['rms_1_(µV)'].to_list()
    rms_2 = csv_file['rms_2_(µV)'].to_list()
    rms_3 = csv_file['rms_3_(µV)'].to_list()
    rms_4 = csv_file['rms_4_(µV)'].to_list()
    total_rms = [rms_1, rms_2, rms_3, rms_4]

    if user_id:
        owner = User.objects.get(id=user_id)
    else:
        owner = User.objects.first()

    for number_of_suite in range(numbers_of_suites):
        suite_name = 'Prueba {}'.format(number_of_suite + 1)
        suite = Suite(owner=owner, name=suite_name)
        suite.save()

        for item in range(2):
            for index in range(4):
                muscle_name = names[index]
                rms = total_rms[index]
                avg_rms = avg_rmss[index]
                mvc = mvcs[index]
                historic_mvc = historic_mvcs[index]
                raw = total_raw[index]
                wave = Wave(muscle=muscle_name, rms=rms, avg_rms=avg_rms, mvc=mvc, historic_mvc=historic_mvc, raw=raw,
                            suite=suite)
                wave.save()
