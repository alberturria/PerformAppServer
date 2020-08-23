# Generated by Django 3.0.3 on 2020-08-22 18:08

from django.db import migrations, models
import django.db.models.deletion
import src.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0011_auto_20200817_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='suite',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'generic'), (2, 'padel'), (3, 'rehab')], default=1),
        ),
        migrations.AddField(
            model_name='suite',
            name='video',
            field=models.FileField(default='rehabilitacion-de-hombro.mp4', storage=src.storage_backends.PrivateMediaStorage(), upload_to='diagnoses'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='video',
            field=models.FileField(default='rehabilitacion-de-hombro.mp4', storage=src.storage_backends.PrivateMediaStorage(), upload_to='diagnoses'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='photo',
            field=models.ImageField(default='blank-profile-picture.png', storage=src.storage_backends.PrivateMediaStorage(), upload_to='patients'),
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=5000)),
                ('suite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='waves.Suite')),
            ],
        ),
    ]
