# Generated by Django 4.1.4 on 2022-12-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaManager', '0004_alter_logmessage_age_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmessage',
            name='description',
            field=models.CharField(default='None', max_length=350),
        ),
        migrations.AddField(
            model_name='logmessage',
            name='duration',
            field=models.IntegerField(default=0, max_length=300),
        ),
    ]
