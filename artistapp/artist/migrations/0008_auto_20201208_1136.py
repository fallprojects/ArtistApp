# Generated by Django 3.1.3 on 2020-12-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0007_auto_20201208_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='slug',
        ),
        migrations.AddField(
            model_name='content',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
