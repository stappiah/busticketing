# Generated by Django 3.2.1 on 2024-09-21 13:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_bus_air_conditioner'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='departure_date',
            field=models.DateField(default=datetime.datetime(2024, 9, 21, 13, 16, 47, 188336, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
