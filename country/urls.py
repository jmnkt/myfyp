from django.urls import path
from .views import country_list, state_based_on_country, country_browse, state_browse

urlpatterns = [
    path('listAllCountry/', country_list, name='country-list'),
    path('browseAllCountry/', country_browse, name='country-browse'),
    path('<country>/browseAllState/', state_browse, name='state-browse'),
    path('<country>/listAllState/', state_based_on_country, name='state-list'),  
]