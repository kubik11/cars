# Generated by Django 3.0.7 on 2023-01-18 22:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('АИ', 'Киевская обл'), ('ВН', 'Одесская обл'), ('ХИ', 'Херсонская обл')], max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('car_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('features', models.CharField(choices=[('Cruise control', 'Cruise control'), ('Airbags', 'Airbags'), ('Audio Interface', 'Audio Interface')], max_length=255)),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmition', models.CharField(max_length=100)),
                ('miles', models.IntegerField()),
                ('doors', models.CharField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], max_length=100)),
                ('passengers', models.CharField(max_length=100)),
                ('milage', models.CharField(max_length=100)),
                ('fuel_type', models.CharField(max_length=100)),
                ('vin_no', models.CharField(max_length=100)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(max_length=100)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 18, 22, 11, 48, 649934))),
            ],
        ),
    ]
