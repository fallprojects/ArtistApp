# Generated by Django 3.1.3 on 2020-12-08 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0008_auto_20201208_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='slug',
        ),
    ]
