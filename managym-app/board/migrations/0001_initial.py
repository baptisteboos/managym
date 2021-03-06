# Generated by Django 3.0.8 on 2020-07-28 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apparatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=3, unique=True)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name': 'Apparatus',
                'verbose_name_plural': 'Apparatus',
            },
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('gender', models.IntegerField(choices=[(1, 'male'), (2, 'female'), (3, 'not specified')], default=3)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=100)),
                ('email_2', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=64, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('province', models.CharField(blank=True, max_length=2, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'verbose_name': 'Athlete',
                'verbose_name_plural': 'Athletes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=120, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='TypeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'TypeEvent',
                'verbose_name_plural': 'TypesEvent',
            },
        ),
        migrations.CreateModel(
            name='TypeInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'TypeInformation',
                'verbose_name_plural': 'TypesInformation',
            },
        ),
        migrations.CreateModel(
            name='TargetResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_sv', models.FloatField(blank=True, null=True)),
                ('target_ex', models.FloatField(blank=True, null=True)),
                ('result_sv', models.FloatField(blank=True, null=True)),
                ('result_ex', models.FloatField(blank=True, null=True)),
                ('apparatus', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='board.Apparatus')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='board.Athlete')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='board.Event')),
            ],
            options={
                'verbose_name': 'TargetResult',
                'verbose_name_plural': 'TargetsResults',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Athlete')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='board.TypeInformation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Information',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New group', max_length=120)),
                ('users', models.ManyToManyField(related_name='groups_of_athletes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Group of athletes',
                'verbose_name_plural': 'Groups of athletes',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.TypeEvent'),
        ),
        migrations.AddField(
            model_name='athlete',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='board.Group'),
        ),
    ]
