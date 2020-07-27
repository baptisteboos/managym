# Generated by Django 3.0.8 on 2020-07-27 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0009_group_users'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='athletes.TypeEvent'),
        ),
    ]
