from django.urls import path 
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from .views import (home, check_option_text, login_view, get_managements)
urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home, name="home"),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

    # couple of view for admin customization
    path('check-option-type/', check_option_text, name='check_option_text'),
    path("get-managements/", get_managements, name="get-managements"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
