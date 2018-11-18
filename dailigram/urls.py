"""dailigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
# from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views
from diary import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('diary/', include('diary.urls')),
    path('', RedirectView.as_view(url='/accounts/login/')),
    path('auth/', include('social_django.urls', namespace='social')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # ex: /diary/login/
    path('login/', views.user_login, name='login'),
    # ex: /diary/logout/
    path('logout/', views.user_logout, name='logout')
]

# if settings.DEBUG: 
    # urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)