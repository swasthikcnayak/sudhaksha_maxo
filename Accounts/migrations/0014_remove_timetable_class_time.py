# Generated by Django 3.1.3 on 2020-12-18 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0013_timetable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='class_time',
        ),
    ]
