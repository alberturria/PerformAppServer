from waves.interfaces.repositories.delete_suite_data_access_interface import DeleteSuiteDataAccessInterface
from waves.models import Suite


class DeleteSuiteDataAccess(DeleteSuiteDataAccessInterface):
    def __init__(self, user_id, suite_id):
        self._user_id = user_id
        self._suite_id = suite_id

    def delete(self):
        suite = Suite.objects.get(id=self._suite_id, owner__id=self._user_id)
        suite.delete()
