# Generated by Django 4.0.6 on 2023-01-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0009_contractfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractfile',
            name='file',
            field=models.URLField(max_length=1000),
        ),
    ]
