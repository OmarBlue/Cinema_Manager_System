# Generated by Django 4.1.4 on 2022-12-18 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaManager', '0002_rename_message_logmessage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmessage',
            name='age_rating',
            field=models.CharField(default='SOME STRING', max_length=30),
        ),
    ]
