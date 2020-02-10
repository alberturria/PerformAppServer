import csv
import pandas as pd

from waves.models import Wave


def read_csv_file(file_path):
    csv_file = pd.read_csv(file_path, sep=';')
    headers = csv_file.columns
    names = csv_file[headers[0]]
    avg_rms = csv_file[headers[1]]
    rms_per_seconds = csv_file[headers[2]]
    mvcs = csv_file[headers[3]]
    historic_mvcs = csv_file[headers[4]]
    waves = Wave.objects.all()
    if len(waves) == 0:
        csv_file = pd.read_csv(file_path, sep=';')
        headers = csv_file.columns
        names = csv_file[headers[0]]
        avg_rmss = csv_file[headers[1]]
        rms_per_seconds = csv_file[headers[2]]
        mvcs = csv_file[headers[3]]
        historic_mvcs = csv_file[headers[4]]

        csv_file_2 = pd.read_csv('./data/advanced_mdurance_1.csv', sep=';')

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

        for item in range(4):
            wave = Wave()
            for index in range(4):
                muscle_name = names[index]
                rms = total_rms[index]
                avg_rms = avg_rmss[index]
                mvc = mvcs[index]
                historic_mvc = historic_mvcs[index]
                raw = total_raw[index]
                wave = Wave(muscle=muscle_name, rms=rms, avg_rms=avg_rms, mvc=mvc, historic_mvc=historic_mvc, raw=raw)
                wave.save()
