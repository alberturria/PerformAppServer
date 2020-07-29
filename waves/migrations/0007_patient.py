# Generated by Django 3.0.3 on 2020-07-27 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0006_auto_20200720_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'other')])),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='patients')),
                ('suite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='waves.Suite')),
            ],
        ),
    ]