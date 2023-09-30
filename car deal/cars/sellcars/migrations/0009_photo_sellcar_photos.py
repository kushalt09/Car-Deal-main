# Generated by Django 4.2.2 on 2023-06-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellcars', '0008_remove_sellcar_photos_alter_sellcar_user_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_photos')),
            ],
        ),
        migrations.AddField(
            model_name='sellcar',
            name='photos',
            field=models.ManyToManyField(to='sellcars.photo'),
        ),
    ]