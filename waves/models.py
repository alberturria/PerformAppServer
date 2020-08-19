from django.contrib.auth.models import User
from django.core.validators import validate_comma_separated_integer_list
from django.db import models
from src.storage_backends import PrivateMediaStorage


class Patient(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    GENDER_MALE, GENDER_FEMALE, GENDER_OTHER_GENDER = 1, 2, 3
    gender = models.PositiveSmallIntegerField(choices=((GENDER_MALE, 'male'), (GENDER_FEMALE, 'female'),
                                                       (GENDER_OTHER_GENDER, 'other')), default=1)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone_number = models.PositiveIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='patients', default='blank-profile-picture.png', storage=PrivateMediaStorage())
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Suite(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    video = models.FileField(upload_to='diagnoses', default='rehabilitacion-de-hombro.mp4',
                             storage=PrivateMediaStorage())
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Wave(models.Model):
    muscle = models.CharField(max_length=255, null=True)
    rms = models.CharField(validators=[validate_comma_separated_integer_list], max_length=5000)
    raw = models.CharField(validators=[validate_comma_separated_integer_list], max_length=500000, default=[])
    avg_rms = models.FloatField()
    mvc = models.FloatField()
    historic_mvc = models.FloatField()
    suite = models.ForeignKey(Suite, on_delete=models.SET_NULL, null=True)


class Diagnosis(models.Model):
    description = models.TextField()
    name = models.CharField(max_length=255)
    video = models.FileField(upload_to='diagnoses', default='rehabilitacion-de-hombro.mp4', storage=PrivateMediaStorage())
    suite = models.ForeignKey(Suite, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class CustomField(models.Model):
    parameter = models.CharField(max_length=255)
    value = models.CharField(max_length=5000)
    suite = models.ForeignKey(Suite, on_delete=models.SET_NULL, null=True)
