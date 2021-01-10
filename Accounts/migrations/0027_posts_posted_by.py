# Generated by Django 3.1.3 on 2021-01-09 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0026_posts_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='posted_by',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]