from django.urls import path,  include
from diary import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required, permission_required

app_name = 'diary'
urlpatterns = [
    
    # ex: /diary/
    path('',  login_required(TemplateView.as_view(template_name="diary/index.html")), name='index'),
    # ex: /diary/register/
    # path('register/', views.UserFormView.as_view(), name = 'register'),
    # ex: /diary/create/
    path('create/', views.CreateView.as_view(), name='create'),
    
]
