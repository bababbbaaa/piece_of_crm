# Generated by Django 4.0.6 on 2023-02-08 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0021_contract_last_status_changed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.contractstatus'),
        ),
    ]
