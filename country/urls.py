from django.urls import path
from .views import country_list, state_based_on_country

urlpatterns = [
    path('listAllCountry/', country_list, name='country-list'),
    path('<country>/listAllState/', state_based_on_country, name='state-list'),  
]