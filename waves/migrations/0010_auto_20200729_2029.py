# Generated by Django 3.0.3 on 2020-07-29 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0009_auto_20200728_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='suite',
        ),
        migrations.AddField(
            model_name='suite',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='waves.Patient'),
        ),
    ]
