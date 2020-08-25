from django.conf.urls import url
from waves.views.create_sample_data_view import CreateSampleDataView
from waves.views.create_user_view import CreateUserView
from waves.views.diagnoses_catalog_view import DiagnosesCatalogView
from waves.views.diagnoses_sample_data_view import DiagnosesSampleDataView
from waves.views.diagnosis_view import DiagnosisView
from waves.views.export_to_pdf_view import ExportToPDFView
from waves.views.fatigue_analysis_view import FatigueAnalysisView
from waves.views.import_data_view import ImportDataView
from waves.views.log_user_view import LogUserView
from waves.views.patient_view import PatientView
from waves.views.patients_catalog_view import PatientsCatalogView
from waves.views.patients_sample_data_view import PatientsSampleDataView
from waves.views.rms_sections_view import RmsSectionsView
from waves.views.send_mail_view import SendMailView
from waves.views.suites_catalog_view import SuitesCatalogView
from waves.views.suites_view import SuitesView
from waves.views.wave_statistics_view import WaveStatisticsView

urlpatterns = [
    url(r'^create-user$', CreateUserView.as_view(), name='create_user'),
    url(r'^log-user$', LogUserView.as_view(), name='log_user'),
    url(r'^import-data/(?P<user_id>\d+)$', ImportDataView.as_view(), name='import_data'),
    url(r'^get-rms-sections/(?P<wave_id>\d+)$', RmsSectionsView.as_view(), name='process_waves'),
    url(r'^(?P<user_id>\d+)/suites-catalog$', SuitesCatalogView.as_view(), name='suites_catalog_view'),
    url(r'^(?P<user_id>\d+)/patients/(?P<patient_id>\d+)$', PatientView.as_view(), name='patient_view'),
    url(r'^(?P<user_id>\d+)/patients$', PatientsCatalogView.as_view(), name='patients_catalog_view'),
    url(r'^(?P<user_id>\d+)/suites/(?P<suite_id>\d+)$', SuitesView.as_view(), name='suites_view'),
    url(r'^(?P<user_id>\d+)/wave-statistics/(?P<suite_id>\d+)$', WaveStatisticsView.as_view(),
        name='wave_statistics_view'),
    url(r'^(?P<user_id>\d+)/fatigue-analysis/(?P<suite_id>\d+)$', FatigueAnalysisView.as_view(),
        name='fatigue_analysis_view'),
    url(r'^(?P<user_id>\d+)/diagnoses$', DiagnosesCatalogView.as_view(), name='diagnoses_catalog_view'),
    url(r'^(?P<user_id>\d+)/diagnoses/(?P<diagnosis_id>\d+)$', DiagnosisView.as_view(), name='diagnosis_view'),
    url(r'^(?P<user_id>\d+)/create-sample-data$', CreateSampleDataView.as_view(), name='sample_data_view'),
    url(r'^(?P<user_id>\d+)/patients-sample-data$', PatientsSampleDataView.as_view(), name='patients_sample_data_view'),
    url(r'^(?P<user_id>\d+)/diagnoses-sample-data$', DiagnosesSampleDataView.as_view(),
        name='diagnoses_sample_data_view'),
    url(r'^(?P<user_id>\d+)/export-to-pdf/(?P<suite_id>\d+)$', ExportToPDFView.as_view(), name='export_to_pdf_view'),
    url(r'^(?P<user_id>\d+)/send-mail/(?P<suite_id>\d+)$', SendMailView.as_view(), name='send_mail_view'),
]
