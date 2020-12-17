# Generated by Django 3.1.3 on 2020-12-08 09:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('TEACHER', 'TEACHER'), ('STUDENT', 'STUDENT')], default='STUDENT', max_length=15)),
                ('Uid', models.CharField(max_length=20)),
                ('image', models.CharField(default=None, max_length=255)),
                ('user_field', models.CharField(choices=[('ENGINEERING', 'ENGINEERING'), ('MEDICAL', 'MEDICAL'), ('OTHER', 'OTHER')], max_length=20)),
                ('date_joined', models.DateField(default=datetime.date.today, verbose_name='date_joined')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
