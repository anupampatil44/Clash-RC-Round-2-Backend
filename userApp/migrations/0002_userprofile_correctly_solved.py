# Generated by Django 3.1.4 on 2021-01-31 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='correctly_solved',
            field=models.IntegerField(default=0),
        ),
    ]