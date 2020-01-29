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

    frames = csv_file['frames_(0.25s)']
    column_1 = csv_file['rms_1_(µV)']
    column_2 = csv_file['rms_2_(µV)']
    column_3 = csv_file['rms_3_(µV)']
    column_4 = csv_file['rms_4_(µV)']

    for item in range(4):
        wave = Wave()

