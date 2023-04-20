# Generated by Django 4.0.6 on 2023-03-23 14:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_promocode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='discount',
            field=models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка'),
        ),
    ]
