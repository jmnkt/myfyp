from django.urls import path
from .views import sendGuideMessage, sendTravelerMessage, traveler_message_received, guide_message_received, guide_message_received_detail, traveler_message_received_detail

urlpatterns = [
    path('<id>/sendGuideMessage/', sendGuideMessage, name='sendGuideMessage'),
    path('<id>/sendTravelerMessage/', sendTravelerMessage, name='sendTravelerMessage'),
    path('listTravelerMessages/', traveler_message_received, name='listTravelerMessage'),
    path('<id>/listGuideMessages/', guide_message_received, name='listGuideMessage'),
    path('<id>/listTravelerMessagesDetail/', traveler_message_received_detail, name='listTravelerMessagesDetail'),
    path('<id>/listGuideMessagesDetail/', guide_message_received_detail, name='listGuideMessagesDetail'),
]