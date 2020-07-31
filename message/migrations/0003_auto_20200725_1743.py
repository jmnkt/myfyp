# Generated by Django 3.0.8 on 2020-07-25 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('message', '0002_auto_20200717_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='messageToGuide',
            fields=[
                ('messagesID', models.AutoField(primary_key=True, serialize=False)),
                ('tripID', models.IntegerField()),
                ('recipientID', models.IntegerField()),
                ('content', models.TextField()),
                ('sendAt', models.DateTimeField(auto_now=True)),
                ('senderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='message',
        ),
    ]