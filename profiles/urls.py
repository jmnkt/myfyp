from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user_profile, name='profileCreate' )
]