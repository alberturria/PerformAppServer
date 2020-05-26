from django.conf.urls import url
from waves.views.rms_sections_view import RmsSectionsView
from waves.views.waves_view import WavesView

urlpatterns = [
    url(r'^get-rms-sections/(?P<wave_id>\d+)$', RmsSectionsView.as_view(), name='process_waves'),
    url(r'$', WavesView.as_view(), name='process_waves'),
]

