import pandas as pd
from waves.interfaces.repositories.read_csv_file_data_access_interface import ReadCSVFileDataAccessInterface
from waves.models import Wave, Suite


class ReadCSVFileDataAccess(ReadCSVFileDataAccessInterface):
    def __init__(self, file, user_id, suite_id):
        self._file = file
        self._user_id = user_id
        self._suite_id = suite_id

    def import_data(self):
        suite = None
        if self._suite_id:
            suite = Suite.objects.get(id=self._suite_id)

        csv_file = pd.read_csv(self._file, sep=';')
        headers = csv_file.columns
        names = csv_file[headers[0]]
        avg_rmss = csv_file[headers[1]]
        mvcs = csv_file[headers[3]]
        historic_mvcs = csv_file[headers[4]]

        raw_1 = csv_file['emg_muscle_1_(µV)']
        raw_1 = raw_1.dropna().to_list()

        raw_2 = csv_file['emg_muscle_2_(µV)']
        raw_2 = raw_2.dropna().to_list()

        raw_3 = csv_file['emg_muscle_3_(µV)']
        raw_3 = raw_3.dropna().to_list()

        raw_4 = csv_file['emg_muscle_4_(µV)']
        raw_4 = raw_4.dropna().to_list()

        total_raw = [raw_1, raw_2, raw_3, raw_4]

        rms_1 = csv_file['rms_1_(µV)']
        rms_1 = rms_1.dropna().to_list()

        rms_2 = csv_file['rms_2_(µV)']
        rms_2 = rms_2.dropna().to_list()

        rms_3 = csv_file['rms_3_(µV)']
        rms_3 = rms_3.dropna().to_list()

        rms_4 = csv_file['rms_4_(µV)']
        rms_4 = rms_4.dropna().to_list()

        total_rms = [rms_1, rms_2, rms_3, rms_4]

        for index in range(4):
            muscle_name = names[index]
            rms = total_rms[index]
            avg_rms = avg_rmss[index]
            mvc = mvcs[index]
            historic_mvc = historic_mvcs[index]
            raw = total_raw[index]
            wave = Wave(muscle=muscle_name, rms=rms, avg_rms=avg_rms, mvc=mvc, historic_mvc=historic_mvc,
                        raw=raw, suite=suite)
            wave.save()
