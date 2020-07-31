# Generated by Django 3.0.8 on 2020-07-21 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_remove_userprofile_guide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guideprofile',
            name='itinerary',
        ),
        migrations.RemoveField(
            model_name='guideprofile',
            name='licenses',
        ),
        migrations.CreateModel(
            name='profilePicImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profilePic', models.ImageField(upload_to='profilePicture')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userProfile')),
            ],
        ),
        migrations.CreateModel(
            name='licenseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licenses', models.FileField(blank=True, null=True, upload_to='license')),
                ('guideID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.guideProfile')),
            ],
        ),
        migrations.CreateModel(
            name='itineraryFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itinerary', models.FileField(upload_to='sampleItinerary')),
                ('guideID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.guideProfile')),
            ],
        ),
    ]