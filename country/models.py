from django.db import models

class Country(models.Model):
    countryCode = models.CharField(primary_key=True, max_length=100)
    countryName = models.CharField(max_length=100)