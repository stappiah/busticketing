# Generated by Django 3.2.1 on 2024-09-26 16:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20240925_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 9, 26, 16, 58, 11, 932835, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
