# Generated by Django 3.1.1 on 2020-10-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0010_auto_20201008_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='testcases',
            field=models.IntegerField(default=2),
        ),
    ]
