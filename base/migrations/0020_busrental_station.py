# Generated by Django 3.2.1 on 2024-09-24 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_busrental_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='busrental',
            name='station',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='base.busstation'),
            preserve_default=False,
        ),
    ]
