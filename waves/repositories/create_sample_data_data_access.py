from common.utils.read_csv import read_csv_file
from waves.interfaces.repositories.create_sample_data_data_access_interface import CreateSampleDataDataAccessInterface


class CreateSampleDataDataAccess(CreateSampleDataDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def create_sample_data(self):
        read_csv_file('./data/basic_mdurance-test.csv', './data/advanced_mdurance_1.csv', self._user_id)