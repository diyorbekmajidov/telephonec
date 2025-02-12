# Generated by Django 4.2.18 on 2025-02-08 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personcontact',
            name='work_phone',
        ),
        migrations.AddField(
            model_name='personcontact',
            name='phone_number',
            field=models.CharField(default='1', max_length=20, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
            preserve_default=False,
        ),
    ]
