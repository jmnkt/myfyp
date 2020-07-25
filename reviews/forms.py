from django import forms
from .models import ReviewsForGuides, ReviewsForTravelers

class ReviewsForGuidesForm(forms.ModelForm):
    class Meta:
        model = ReviewsForGuides
        fields = [
            'reviewContent',
            'rating',
        ]
        
class ReviewsForTravelersForm(forms.ModelForm):
    class Meta:
        model = ReviewsForTravelers
        fields = [
            'reviewContent',
            'rating',
        ]

