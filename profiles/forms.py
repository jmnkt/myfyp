from django import forms
from .models import userProfile, guideProfile, itineraryFile, licenseFile, profilePicImage 

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = [
            'name',
            'gender',
            'passportNo',
            'email',
            'address',
            'dateOfBirth',
            'identity',
        ]

class GuideProfileForm(forms.ModelForm):
    class Meta:
        model = guideProfile
        fields = [
            # 'userProfiles',
            'guidingCountry',
            'guidingState',
            'introduction',
            'position',
            'quotedCharges'
        ]

class ItineraryModelForm(forms.ModelForm):
    class Meta:
        model = itineraryFile
        fields = ['itinerary']

class LicenseModelForm(forms.ModelForm):
    class Meta:
        model = licenseFile
        fields = ['licenses']
        
class ProfilePicModelForm(forms.ModelForm):
    class Meta:
        model = profilePicImage
        fields = ['profilePic']