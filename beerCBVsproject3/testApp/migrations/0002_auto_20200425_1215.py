# Generated by Django 3.0.5 on 2020-04-25 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='price',
            field=models.FloatField(),
        ),
    ]