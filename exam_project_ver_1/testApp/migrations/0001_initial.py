# Generated by Django 3.0.5 on 2020-06-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email Address')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('contact_number', models.IntegerField(default=0)),
                ('profile_pic', models.ImageField(upload_to='pics')),
                ('course', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date_joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_speruser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
