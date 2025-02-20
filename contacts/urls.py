from django.urls import path 
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from .views import (home, check_option_text, login_view, get_managements, home1, home2)
urlpatterns = [
    path('login/', login_view, name='login'),
    path('', home1, name="home"),
    path('home/', home2),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('check-option-type/', check_option_text, name='check_option_text'),
    path("get-managements/", get_managements, name="get-managements"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
