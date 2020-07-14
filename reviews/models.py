from django.db import models
from profiles.models import Travelers, Guides

# Create your models here.

class travelerReviews(models.Model):
    reviewID = models.AutoField(primary_key = True)
    senderID = models.ForeignKey('Traveler', on_delete = models.CASCADE)
    tripID = models.ForeignKey('Trip', on_delete = models.CASCADE)
    GuideID = models.ForeignKey('Guides', on_delete = models.CASCADE )
    reviewContent = models.TextField()
    rating_Choices = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]
    rating = models.IntegerField(choices = rating_Choices, default = 1)

class guideReviews(models.Model):
    reviewID = models.AutoField(primary_key = True)
    senderID = models.ForeignKey('Guides', on_delete = models.CASCADE )
    tripID = models.ForeignKey('Trip', on_delete = models.CASCADE)
    travelerID = models.ForeignKey('Traveler', on_delete = models.CASCADE)
    reviewContent = models.TextField()
    rating_Choices = [
        (1, 'Poor'),
        (2, 'Average'),
        (3, 'Good'),
        (4, 'Very Good'),
        (5, 'Excellent')
    ]
    rating = models.IntegerField(choices = rating_Choices, default = 1)