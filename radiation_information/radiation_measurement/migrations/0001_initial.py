# Generated by Django 3.1.6 on 2021-02-01 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radiation_measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instrument_name', models.CharField(blank=True, max_length=50, null=True)),
                ('measured_value_EF', models.CharField(default='EF V/m', editable=False, max_length=10)),
                ('EF_measured_value', models.CharField(max_length=30)),
                ('measured_value_MF', models.CharField(default='MF μT', editable=False, max_length=10)),
                ('MF_measured_value', models.CharField(max_length=30)),
                ('measured_value_Power', models.CharField(default='Power mW/cm2', editable=False, max_length=10)),
                ('Power_measured_value', models.CharField(max_length=30)),
                ('threshold_distance_EF', models.CharField(default='MF', editable=False, max_length=10)),
                ('EF_threshold_distance', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.place')),
            ],
        ),
    ]