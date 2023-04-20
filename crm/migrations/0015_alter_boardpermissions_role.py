# Generated by Django 4.0.6 on 2023-01-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0014_boardinvite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardpermissions',
            name='role',
            field=models.CharField(choices=[('OWN', 'Owner'), ('ADMIN', 'ADMIN'), ('EMPL', 'Employee')], max_length=25),
        ),
    ]
