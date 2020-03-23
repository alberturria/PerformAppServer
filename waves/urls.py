from django.conf.urls import url
from waves.views.process_waves_view import ProcessWavesView
from waves.views.waves_view import WavesView

urlpatterns = [
    url(r'$', WavesView.as_view(),
        name='process_waves')]
