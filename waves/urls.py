from django.conf.urls import url
from waves.views.create_sample_data_view import CreateSampleDataView
from waves.views.create_user_view import CreateUserView
from waves.views.export_to_pdf_view import ExportToPDFView
from waves.views.import_data_view import ImportDataView
from waves.views.log_user_view import LogUserView
from waves.views.patient_view import PatientView
from waves.views.patients_catalog_view import PatientsCatalogView
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
    url(r'^(?P<user_id>\d+)/patients/(?P<patient_id>\d+)$', PatientView.as_view(), name='patient_view'),
    url(r'^(?P<user_id>\d+)/patients$', PatientsCatalogView.as_view(), name='patients_catalog_view'),
    url(r'^(?P<user_id>\d+)/suites/(?P<suite_id>\d+)$', SuitesView.as_view(), name='suites_view'),
    url(r'^(?P<user_id>\d+)/create-sample-data$', CreateSampleDataView.as_view(), name='sample_data_view'),
    url(r'^(?P<user_id>\d+)/export-to-pdf/(?P<suite_id>\d+)$', ExportToPDFView.as_view(), name='export_to_pdf_view'),
    url(r'$', WavesView.as_view(), name='process_waves'),
]
