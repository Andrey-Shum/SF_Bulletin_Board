from django.urls import path
from . import views

app_name = 'appAccounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
] 