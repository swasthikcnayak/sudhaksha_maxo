# Generated by Django 3.1.3 on 2021-01-09 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0025_auto_20210109_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='description',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
