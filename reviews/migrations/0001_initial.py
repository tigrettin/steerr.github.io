# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('model_platform_years', models.CharField(max_length=50)),
                ('model_body_platform_years', models.CharField(max_length=50)),
                ('model_version', models.CharField(max_length=50)),
                ('model_version_description_years', models.CharField(max_length=50)),
                ('source_of_data', models.CharField(max_length=50)),
                ('years_sold', models.CharField(max_length=50)),
                ('sold_in_europe', models.CharField(max_length=50)),
                ('car_classification', models.CharField(max_length=50)),
                ('body_type', models.CharField(max_length=50)),
                ('no_of_doors', models.IntegerField(default=0)),
                ('no_of_seats', models.IntegerField(default=0)),
                ('engine_place', models.CharField(max_length=50)),
                ('drivetrain', models.CharField(max_length=50)),
                ('cylinders', models.CharField(max_length=50)),
                ('displacement_cm3', models.IntegerField(default=0)),
                ('power_kw', models.IntegerField(default=0)),
                ('power_ps', models.IntegerField(default=0)),
                ('power_rpm', models.IntegerField(default=0)),
                ('torque_nm', models.IntegerField(default=0)),
                ('torque_rpm', models.IntegerField(default=0)),
                ('bore_stroke_mm', models.CharField(max_length=50)),
                ('compression_ratio', models.FloatField(default=0)),
                ('valves_per', models.IntegerField(default=0)),
                ('crankshaft', models.CharField(max_length=50)),
                ('fuel_injection', models.CharField(max_length=50)),
                ('supercharger', models.CharField(max_length=50)),
                ('catalytic', models.CharField(max_length=50)),
                ('manual', models.IntegerField(default=0)),
                ('automatic', models.CharField(max_length=50)),
                ('suspension_front', models.CharField(max_length=50)),
                ('suspension_rear', models.CharField(max_length=50)),
                ('assisted', models.CharField(max_length=50)),
                ('turning_circle_m', models.IntegerField(default=0)),
                ('brakes_front', models.CharField(max_length=50)),
                ('brakes_rear', models.CharField(max_length=50)),
                ('brakes_abs', models.CharField(max_length=50)),
                ('esp', models.CharField(max_length=50)),
                ('tire_size', models.CharField(max_length=50)),
                ('tire_size_rear', models.CharField(max_length=50)),
                ('wheel_base_mm', models.IntegerField(default=0)),
                ('track_front_mm', models.IntegerField(default=0)),
                ('track_rear_mm', models.IntegerField(default=0)),
                ('length_mm', models.IntegerField(default=0)),
                ('width_mm', models.IntegerField(default=0)),
                ('height_mm', models.IntegerField(default=0)),
                ('curb_weight_kg', models.IntegerField(default=0)),
                ('gross_weight_kg', models.IntegerField(default=0)),
                ('load_kg', models.IntegerField(default=0)),
                ('stutzlast_kg', models.IntegerField(default=0)),
                ('rooaf_load_kg', models.IntegerField(default=0)),
                ('cargo_space_litres', models.CharField(max_length=50)),
                ('tow_weight_kg', models.CharField(max_length=50)),
                ('gas_tank_litres', models.IntegerField(default=0)),
                ('_100_kmph_sec', models.FloatField(default=0)),
                ('max_speed_kmh', models.IntegerField(default=0)),
                ('fuel_eff_l100km', models.FloatField(default=0)),
                ('fuel_eff_city_l100km', models.FloatField(default=0)),
                ('fuel_eff_highway', models.FloatField(default=0)),
                ('engine_type', models.CharField(max_length=50)),
                ('fuel_type', models.CharField(max_length=50)),
                ('co2_gkm', models.IntegerField(default=0)),
                ('co2_efficiency_class', models.CharField(max_length=50)),
                ('pollution_class', models.CharField(max_length=50)),
                ('base_price_in_germany', models.IntegerField(default=0)),
            ],
        ),
    ]
