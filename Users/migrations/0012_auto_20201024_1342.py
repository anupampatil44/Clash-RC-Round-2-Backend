# Generated by Django 3.1.2 on 2020-10-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20201023_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='totalSubmision',
            field=models.IntegerField(default=0),
        ),
    ]
