# Generated by Django 3.0.8 on 2020-07-17 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20200717_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='GuideID',
        ),
    ]