# Generated by Django 4.2.2 on 2023-06-06 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('name', models.ImageField(upload_to='media/carz/%Y/%m/')),
                ('video_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('company_name', models.CharField(max_length=255)),
                ('categories', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('kms_driven', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
