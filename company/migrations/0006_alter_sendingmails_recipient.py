# Generated by Django 4.0.4 on 2022-09-07 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('company', '0005_alter_contact_options_userscontacts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendingmails',
            name='recipient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.userscontacts',
                                    verbose_name='Recipient'),
        ),
    ]
