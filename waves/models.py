from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
from django.db import models


class Suite(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Wave(models.Model):
    muscle = models.CharField(max_length=255, null=True)
    rms = models.CharField(validators=[validate_comma_separated_integer_list], max_length=500)
    raw = models.CharField(validators=[validate_comma_separated_integer_list], max_length=500, default=[])
    avg_rms = models.FloatField()
    mvc = models.FloatField()
    historic_mvc = models.FloatField()
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE, null=True)
