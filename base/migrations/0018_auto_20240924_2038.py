# Generated by Django 3.2.1 on 2024-09-24 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rentalrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busrental',
            name='price',
        ),
        migrations.AddField(
            model_name='rentalprice',
            name='rental',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.busrental'),
            preserve_default=False,
        ),
    ]
