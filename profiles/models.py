from django.db import models


class User(models.Model):
    userID = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    FEMALE = 'F'
    MALE = 'M'
    UNDEFINED = 'U'
    gender_Choices = [
       (FEMALE,'Female'),
       (MALE,'Male'),
       (UNDEFINED,'Undefined'),
    ]
    gender = models.CharField(
        max_length = 1,
        choices = gender_Choices,
        default = UNDEFINED,
    )
    passportNo = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 254)
    address = models.CharField(max_length = 300)
    dateOfBirth = models.DateField()
    profilePic = models.ImageField(upload_to = 'profilePicture')  
   
    

class Guides(models.Model):
    userID = models.ForeignKey('User', on_delete = models.CASCADE)
    guidingCountry = models.ForeignKey('country.Country', on_delete = models.CASCADE)
    guidesID = models.AutoField(primary_key = True) 
    licenses = models.FileField(upload_to = 'license', blank = True, null = True)
    itinerary = models.FileField(upload_to = 'sampleItinerary')
    introduction = models.TextField()

class Travelers(models.Model):
    userID = models.ForeignKey('User', on_delete = models.CASCADE)