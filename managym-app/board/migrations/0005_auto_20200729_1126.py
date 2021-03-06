# Generated by Django 3.0.8 on 2020-07-29 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_athlete_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetresult',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='targets_results', to='board.Event'),
        ),
        migrations.AlterUniqueTogether(
            name='targetresult',
            unique_together={('athlete', 'apparatus', 'event')},
        ),
    ]
