# Generated by Django 4.2.4 on 2023-12-27 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0023_rename_owner_sendoptions_options_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='status_try',
            field=models.CharField(max_length=20, verbose_name='статус попытки'),
        ),
    ]
