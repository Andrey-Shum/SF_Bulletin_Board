from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    """Главная страница"""
    return render(request, 'home.html')

@login_required
def profile(request):
    """Страница профиля пользователя"""
    return render(request, 'account/profile.html')
