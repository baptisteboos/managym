# Generated by Django 3.0.8 on 2020-07-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0003_auto_20200727_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='birth_date',
            field=models.DateField(),
        ),
    ]