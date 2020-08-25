from django.contrib.auth.models import User
from django.core.files import File
from waves.interfaces.repositories.create_sample_data_data_access_interface import CreateSampleDataDataAccessInterface
from waves.models import Suite, CustomField
from waves.repositories.read_csv_file_data_access import ReadCSVFileDataAccess


class CreateSampleDataDataAccess(CreateSampleDataDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def create_sample_data(self):
        owner = User.objects.get(id=self._user_id)
        suite1 = Suite(name='Prueba 1', patient=None,
                      owner=owner)


        suite1.save()

        read_csv_data_access = ReadCSVFileDataAccess('./data/sample-data.csv', self._user_id, suite1.id)
        read_csv_data_access.import_data()

        custom_field = CustomField(parameter='Altura', value='180 cm',
                                   suite=suite1)
        custom_field.save()

        suite2 = Suite(name='Prueba 2', patient=None,
                       owner=owner, type=2)

        suite2.save()

        read_csv_data_access = ReadCSVFileDataAccess('./data/sample-data.csv', self._user_id, suite2.id)
        read_csv_data_access.import_data()

        custom_field = CustomField(parameter='Anotación', value='La segunda repetición del paciente no se ha realizado satisfactoriamente',
                                   suite=suite2)
        custom_field.save()

        suite3 = Suite(name='Prueba 3', patient=None,
                       owner=owner, type=3)

        suite3.save()

        read_csv_data_access = ReadCSVFileDataAccess('./data/sample-data.csv', self._user_id, suite3.id)
        read_csv_data_access.import_data()

