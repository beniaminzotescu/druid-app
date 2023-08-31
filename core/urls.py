from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('enterprise/', views.enterprise, name='enterprise'),
    path('industrial/', views.industrial, name='industrial'),
    path('platinum/', views.platinum, name='platinum'),
    path('gold/', views.gold, name='gold'),
    path('silver/', views.silver, name='silver'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('thank-you/', views.thank_you, name='thank_you'),  # Add this line

]
