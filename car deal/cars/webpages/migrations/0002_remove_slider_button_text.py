# Generated by Django 4.2.2 on 2023-06-16 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='button_text',
        ),
    ]
