# Generated by Django 3.1.3 on 2020-12-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_auto_20201216_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='c_url',
            field=models.URLField(default=None, null=True),
        ),
    ]
