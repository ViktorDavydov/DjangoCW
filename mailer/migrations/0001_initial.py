# Generated by Django 5.0 on 2023-12-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.CharField(max_length=30, verbose_name='контактный email')),
                ('client_name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('comment', models.TextField(verbose_name='комментарий')),
            ],
        ),
    ]
