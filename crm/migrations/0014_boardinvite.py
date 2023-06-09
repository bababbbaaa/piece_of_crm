# Generated by Django 4.0.6 on 2023-01-28 19:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0013_alter_contractstatus_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardInvite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PEND', 'Pending'), ('ACPT', 'Accepted'), ('DEND', 'Denied')],
                                            default='PEND', max_length=128)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
