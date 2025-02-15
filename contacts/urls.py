from django.urls import path 
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from .views import (home, check_option_text, contact_list)
urlpatterns = [
    path('', home),
    path('check-option-type/', check_option_text, name='check_option_text'),
    path('contact-list/', contact_list)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
