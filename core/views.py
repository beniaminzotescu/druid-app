from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from druid_app import settings


@login_required
def index(request):
    return render(request, 'core/index.html')


def logout_view(request):
    response = redirect('/thank-you/')  # Redirect to thank you page
    response.set_cookie('logged_out', 'true', max_age=settings.LOG_OUT_COOKIE_DURATION)
    return response


def thank_you(request):
    return render(request, 'core/thank_you.html')
