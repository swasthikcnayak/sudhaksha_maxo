# Generated by Django 3.1.3 on 2021-01-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0023_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='notes',
            field=models.FileField(null=True, upload_to='media'),
        ),
    ]