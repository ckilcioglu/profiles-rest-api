# Generated by Django 2.1.15 on 2021-09-15 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user',
            new_name='user_profile',
        ),
    ]
