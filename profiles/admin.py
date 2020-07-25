from django.contrib import admin
from .models import userProfile, guideProfile, licenseFile, profilePicImage

admin.site.register(guideProfile)
admin.site.register(userProfile)
admin.site.register(licenseFile)
admin.site.register(profilePicImage)