# Generated by Django 3.0.8 on 2020-07-16 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200716_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
