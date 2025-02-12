# Generated by Django 4.2.18 on 2025-02-10 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_rename_status_personcontact_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectorLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('district', models.CharField(choices=[(109, 'Bulung‘ur tumani'), (110, 'Jomboy tumani'), (111, 'Ishtixon tumani'), (112, 'Kattaqo‘rg‘on tumani'), (113, 'Kattaqo‘rg‘on shahri'), (114, 'Qo‘shrabot tumani'), (115, 'Narpay tumani'), (116, 'Nurabod tumani'), (117, 'Oqdaryo tumani'), (118, 'Payariq tumani'), (119, 'Pastarg‘om tumani'), (120, 'Paxtachi tumani'), (121, 'Samarqand tumani'), (122, 'Samarqand shahri'), (123, 'Toyloq tumani'), (124, 'Urgut tumani')], max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='personcontact',
            name='status',
            field=models.CharField(choices=[('1', 'Sektor Rahbar'), ('2', 'Aparat hodim'), ('3', 'Boshqa')], default=3, max_length=20),
        ),
    ]
