from django.conf.urls import url
from waves.views.process_waves_view import ProcessWavesView

urlpatterns = [
    url(r'$', ProcessWavesView.as_view(),
        name='process_waves')]
