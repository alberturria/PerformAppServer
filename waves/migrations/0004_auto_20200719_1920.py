# Generated by Django 3.0.3 on 2020-07-19 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0003_auto_20200629_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wave',
            name='suite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='waves.Suite'),
        ),
    ]
