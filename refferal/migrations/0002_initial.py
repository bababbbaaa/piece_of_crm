# Generated by Django 4.0.4 on 2022-08-23 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('refferal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitemodel',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.companymodel'),
        ),
    ]
