# Generated by Django 4.0.6 on 2023-01-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0019_boardpermissions_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardpermissions',
            name='description',
        ),
        migrations.AddField(
            model_name='boardlog',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
