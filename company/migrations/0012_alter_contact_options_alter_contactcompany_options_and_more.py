# Generated by Django 4.0.6 on 2023-02-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_alter_sendingmails_options_sendingtelegram'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-id',), 'verbose_name': 'Контакт (наш, т.е внутренний, не созданный пользователем)', 'verbose_name_plural': 'Контакт (наши, т.е внутренние)'},
        ),
        migrations.AlterModelOptions(
            name='contactcompany',
            options={'ordering': ('-id',), 'verbose_name': 'Компания контакта', 'verbose_name_plural': 'Компании контактов'},
        ),
        migrations.AlterModelOptions(
            name='findemails',
            options={'ordering': ('-id',), 'verbose_name': 'Найденная почта', 'verbose_name_plural': 'Найденные почты'},
        ),
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ('-id',), 'verbose_name': 'Список', 'verbose_name_plural': 'Списки'},
        ),
        migrations.AlterModelOptions(
            name='listcontainer',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='newslettertemplate',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='requestsforsearch',
            options={'ordering': ('-id',), 'verbose_name': 'Запрос с поиска', 'verbose_name_plural': 'Запросы с поиска'},
        ),
        migrations.AlterModelOptions(
            name='sendingmails',
            options={'ordering': ('-id',), 'verbose_name': 'Письмо для отправки (Email)', 'verbose_name_plural': 'Письма для отправки (Email)'},
        ),
        migrations.AlterModelOptions(
            name='sendingtelegram',
            options={'ordering': ('-id',), 'verbose_name': 'Письмо для отправки (Telegram)', 'verbose_name_plural': 'Письма для отправки (Telegram)'},
        ),
        migrations.AlterModelOptions(
            name='template',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='userscontacts',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='contact',
            name='telegram_id',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='userscontacts',
            name='telegram_id',
            field=models.CharField(default=None, max_length=128, null=True),
        ),
    ]
