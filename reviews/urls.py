from django.urls import path
from .views import leaveTravelerReview, leaveGuideReview, traveler_review_received, guide_review_received

urlpatterns = [
    path('<id>/leaveTravelerReview/', leaveTravelerReview, name='leaveTravelerReview' ),
    path('<id>/leaveGuideReview/', leaveGuideReview, name='leaveGuideReview' ),
    path('listTravelerReview/', traveler_review_received, name='listTravelerReview'),
    path('<id>/listGuideReview/', guide_review_received, name='listGuideReview'),
]