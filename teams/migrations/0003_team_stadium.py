# Generated by Django 4.1.1 on 2022-09-19 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stadiums', '0001_initial'),
        ('teams', '0002_alter_team_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='stadium',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stadiums.stadium'),
        ),
    ]
