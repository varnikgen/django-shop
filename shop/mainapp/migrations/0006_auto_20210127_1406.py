# Generated by Django 3.1.5 on 2021-01-27 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210127_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baths',
            options={'managed': True, 'verbose_name': 'Ванна', 'verbose_name_plural': 'Ванны'},
        ),
        migrations.AlterModelTable(
            name='baths',
            table='',
        ),
    ]
