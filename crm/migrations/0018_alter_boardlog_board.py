# Generated by Django 4.0.6 on 2023-01-30 22:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('crm', '0017_boardlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardlog',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='crm.board'),
        ),
    ]
