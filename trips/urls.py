from django.urls import path
from .views import trip_create, trip_based_on_traveler, trip_detail, trip_based_on_guide, select_guide, trip_status, trip_update_guide, trip_detail_guides

urlpatterns = [
    path('createNewTrip/', trip_create, name='trip-create'),
    path('<id>/listUpcomingTrip/', trip_based_on_traveler, name='upcoming-trip-list'),
    path('<id>/listTripDetail/', trip_detail, name='trip-detail'),
    path('<id>/listTripDetailForGuides/', trip_detail_guides, name='trip-detail-guides'),
    path('<id>/listIncomingTrip/', trip_based_on_guide, name='incoming-trip-list'),
    path('<id>/selectGuide/', select_guide , name='select-guide'),
    path('<id>/listTripStatus/', trip_status, name='trip-status'),
    path('<id>/updateIncomingTrip/', trip_update_guide, name='trip-update-guide'),
    
]