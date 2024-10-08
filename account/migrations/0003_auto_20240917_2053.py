# Generated by Django 3.2.1 on 2024-09-17 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20240917_2053'),
        ('account', '0002_account_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.RemoveField(
            model_name='account',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='account',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='account',
            name='region',
        ),
        migrations.AddField(
            model_name='account',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='station_users', to='base.busstation'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(default='0551878700', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Administrator'), ('passenger', 'Passenger')], default='passenger', max_length=10),
        ),
    ]
