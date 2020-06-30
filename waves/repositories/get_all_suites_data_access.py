from waves.entities.suite_entity import SuiteEntity
from waves.interfaces.repositories.get_all_suites_data_access_interface import GetAllSuitesDataAccessInterface
from waves.models import Suite


class GetAllSuitesDataAccess(GetAllSuitesDataAccessInterface):
    def __init__(self, user_id):
        self._user_id = user_id

    def get_suites(self):
        suites = Suite.objects.filter(owner__id=self._user_id)
        result = []

        for suite in suites:
            suite_entity = SuiteEntity(suite.id, suite.name, suite.date, suite.owner.id, suite.owner.username)
            result.append(suite_entity)

        return result
