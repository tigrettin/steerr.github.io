# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-20 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20170720_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='_100_kmph_sec',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='assisted',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='automatic',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='base_price_in_germany',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='bore_stroke_mm',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='brakes_abs',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='brakes_front',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='brakes_rear',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_classification',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='cargo_space_litres',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='catalytic',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='co2_efficiency_class',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='co2_gkm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='compression_ratio',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='crankshaft',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='curb_weight_kg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='cylinders',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='displacement_cm3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='drivetrain',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_place',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='esp',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_eff_city_l100km',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_eff_highway',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_eff_l100km',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_injection',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='gas_tank_litres',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='gross_weight_kg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='height_mm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='length_mm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='load_kg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='manual',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='max_speed_kmh',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_body_platform_years',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_platform_years',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_version',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='model_version_description_years',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_of_doors',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='no_of_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='pollution_class',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_kw',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_ps',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='power_rpm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='rooaf_load_kg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='sold_in_europe',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='source_of_data',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='stutzlast_kg',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='supercharger',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='suspension_front',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='suspension_rear',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='tire_size',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='tire_size_rear',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='torque_nm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='torque_rpm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='tow_weight_kg',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='track_front_mm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='track_rear_mm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='turning_circle_m',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='valves_per',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='wheel_base_mm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='width_mm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='years_sold',
            field=models.CharField(max_length=50),
        ),
    ]