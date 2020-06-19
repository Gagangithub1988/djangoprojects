# Generated by Django 3.0.5 on 2020-05-11 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobApp', '0003_auto_20200511_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bangalore_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('eligibility', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phnno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hyderabad_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('eligibility', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phnno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mumbai_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('eligibility', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phnno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pune_jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('company', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('eligibility', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('phnno', models.IntegerField()),
            ],
        ),
    ]
