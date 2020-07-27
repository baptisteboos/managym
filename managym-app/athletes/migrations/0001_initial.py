# Generated by Django 3.0.8 on 2020-07-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'not specified')], default=3)),
                ('birth_date', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=100)),
                ('email_2', models.EmailField(max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('phone_number_2', models.CharField(max_length=15, null=True)),
                ('address', models.CharField(max_length=64, null=True)),
                ('city', models.CharField(max_length=64, null=True)),
                ('province', models.CharField(max_length=2, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Athlete',
                'verbose_name_plural': 'Athletes',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
    ]