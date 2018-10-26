from django.urls import path
from diary import views

app_name =  'diary'
urlpatterns = [
     # ex: /diary/
    path('', views.IndexView.as_view(), name='index'),
     # ex: /diary/register/
    path('register/', views.UserFormView.as_view(), name = 'register'),
]