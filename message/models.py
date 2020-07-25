from django.db import models
from profiles.models import guideProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class messageToGuide(models.Model):
    messagesID = models.AutoField(primary_key = True)
    tripID = models.IntegerField()
    recipientID = models.IntegerField()
    senderID = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sendAt = models.DateTimeField(auto_now = True)

class messageToTraveler(models.Model):
    messagesID = models.AutoField(primary_key = True)
    tripID = models.IntegerField()
    recipientID = models.IntegerField()
    senderID = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sendAt = models.DateTimeField(auto_now = True)

class itineraryFile(models.Model):
   itinerary = models.FileField(upload_to = 'sampleItinerary', blank = True, null = True) 
   messagesID = models.IntegerField()
    