# Generated by Django 3.1.7 on 2021-04-27 01:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recaafilm', '0003_auto_20210426_1821'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Watcher',
            new_name='Customer',
        ),
    ]
