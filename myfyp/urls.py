from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from profiles.views import home
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from profiles.views import home

urlpatterns = [
    path('', home , name='home'),
    path('profiles/', include('profiles.urls')),
    path('reviews/', include('reviews.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('country/', include('country.urls')),
    path('trip/', include('trips.urls')),
    path('message/', include('message.urls')),
    path('reviews/', include('reviews.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

