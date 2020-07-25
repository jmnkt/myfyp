from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from country.models import Country, State
from django.contrib.auth import get_user_model


User = get_user_model()
    
class userProfile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    userID = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    FEMALE = 'F'
    MALE = 'M'
    UNDEFINED = 'U'
    genderChoices = [
       (FEMALE,'Female'),
       (MALE,'Male'),
       (UNDEFINED,'Undefined'),
    ]
    gender = models.CharField(
        max_length = 1,
        choices = genderChoices,
        default = UNDEFINED,
    )
    passportNo = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    address = models.CharField(max_length = 300)
    dateOfBirth = models.DateField()
    identityChoices = [
        ('GUIDES', 'Guides'),
        ('TRAVELERS', 'Travelers'),
    ]
    identity = models.CharField(
        max_length = 30,
        choices = identityChoices,
        default = 'Travelers',
    )
    
    def __str__(self):
        return self.owner.username

class guideProfile(models.Model):
    guidesID = models.AutoField(primary_key = True) 
    # userProfiles = models.ForeignKey(userProfile, on_delete = models.CASCADE)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    guidingCountry = models.ForeignKey('country.Country', on_delete = models.SET_DEFAULT, default = 0000)
    guidingState = models.ForeignKey('country.State', on_delete = models.SET_DEFAULT, default = 0000)
    introduction = models.TextField()
    positionChoices = [
        ('GUIDES', 'Guides'),
        ('PLANNERS', 'Planners')
    ]
    position = models.CharField(
        max_length = 30,
        choices = positionChoices,
        default = 'PLANNERS',
    )
    applicationStatusChoices = [
        ('APPROVED', 'Approved by Admins'),
        ('REJECTED', 'Rejected by Admins'),
        ('PENDING', 'Pending for Approval' )
    ]
    applicationStatus = models.CharField(
        max_length = 30,
        choices = applicationStatusChoices,
        default = 'PENDING',
    )
    quotedCharges = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.user.username

class profilePicImage(models.Model):
   profilePic = models.ImageField(upload_to = 'profilePicture')  
   userID = models.ForeignKey('userProfile', on_delete = models.CASCADE)
   def __str__(self):
        return self.userID.owner.username
    
class itineraryFile(models.Model):
   itinerary = models.FileField(upload_to = 'sampleItinerary') 
   guideID = models.ForeignKey('guideProfile', on_delete = models.CASCADE)
   
class licenseFile(models.Model):
   licenses = models.FileField(upload_to = 'license', blank = True, null = True)
   guideID = models.ForeignKey('guideProfile', on_delete = models.CASCADE)
   def __str__(self):
        return self.guideID.user.username
    
class Travelers(models.Model):
    travelersID = models.AutoField(primary_key = True) 
    userID = models.ForeignKey('userProfile', on_delete = models.CASCADE)