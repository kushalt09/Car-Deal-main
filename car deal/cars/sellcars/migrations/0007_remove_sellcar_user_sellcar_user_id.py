from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellcars', '0006_remove_sellcar_user_id_sellcar_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellcar',
            name='user',
        ),
        migrations.AddField(
            model_name='sellcar',
            name='user_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
