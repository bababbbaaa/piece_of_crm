# Generated by Django 4.0.6 on 2022-12-27 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('company', '0008_alter_sendingmails_link_alter_sendingmails_theme'),
        ('crm', '0005_contractlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='company.userscontacts'),
        ),
    ]
