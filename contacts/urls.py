from django.urls import path 
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from .views import (home, check_option_text, contact_list)
urlpatterns = [
    path('', home),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('check-option-type/', check_option_text, name='check_option_text'),
    path('contact-list/', contact_list)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
