from django.urls import path
from .views import userprofile_create, signup, guideprofile_create, userprofile_detail, guide_based_on_state, guideprofile_detail_travelers, guideprofile_detail

urlpatterns = [
    path('signUp/', signup, name='signup'),
    path('createUserProfile/', userprofile_create, name='user-profile-create'),
    path('createGuideProfile/', guideprofile_create, name='guide-profile-create'),
    path('<id>/userProfileDetail/', userprofile_detail, name='user-profile-detail'),
    path('<id>/listAllGuides/', guide_based_on_state, name='guide-profile-list'),
    path('<id>/guideProfileDetail/', guideprofile_detail, name='guide-profile-detail'),
    path('<id>/guideProfileDetailForTravelers/', guideprofile_detail_travelers, name='guide-profile-detail-travelers'),
    
]