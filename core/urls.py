from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from druid_app import settings
from .forms import LoginForm
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm),
         name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('thank-you/', views.thank_you, name='thank_you'),  # Add this line

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
