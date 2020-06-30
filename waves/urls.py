from django.conf.urls import url
from waves.views.create_user_view import CreateUserView
from waves.views.import_data_view import ImportDataView
from waves.views.log_user_view import LogUserView
from waves.views.rms_sections_view import RmsSectionsView
from waves.views.suites_catalog_view import SuitesCatalogView
from waves.views.suites_view import SuitesView
from waves.views.waves_view import WavesView

urlpatterns = [
    url(r'^create-user$', CreateUserView.as_view(), name='create_user'),
    url(r'^log-user$', LogUserView.as_view(), name='log_user'),
    url(r'^import-data/(?P<user_id>\d+)$', ImportDataView.as_view(), name='import_data'),
    url(r'^get-rms-sections/(?P<wave_id>\d+)$', RmsSectionsView.as_view(), name='process_waves'),
    url(r'^(?P<user_id>\d+)/suites-catalog$', SuitesCatalogView.as_view(), name='suites_catalog_view'),
    url(r'^(?P<user_id>\d+)/suites/(?P<suite_id>\d+)$', SuitesView.as_view(), name='suites_view'),
    url(r'$', WavesView.as_view(), name='process_waves'),
]

