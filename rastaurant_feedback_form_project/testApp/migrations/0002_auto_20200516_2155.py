# Generated by Django 3.0.5 on 2020-05-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rastaurant_feedback',
            name='comment',
            field=models.TextField(max_length=256),
        ),
    ]