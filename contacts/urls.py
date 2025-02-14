from django.urls import path 
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from .views import (home, check_option_text)
urlpatterns = [
    path('', home),
    path('your-view-url/', check_option_text, name='check_option_text'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
