from django.db import models


class Wave(models.Model):
    muscle = models.CharField(max_length=255, null=True)
    rms = models.CommaSeparatedIntegerField()
    avg_rms = models.FloatField()
    mvc = models.FloatField()
    historic_mvc = models.FloatField()
