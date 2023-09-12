from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from druid_app import settings
from django.http import HttpResponse

@login_required
def index(request):
    return render(request, 'core/index.html')


@login_required
def enterprise(request):
    return render(request, 'core/enterprise.html')


@login_required
def industrial(request):
    return render(request, 'core/industrial.html')


@login_required
def platinum(request):
    return render(request, 'core/platinum.html')


@login_required
def gold(request):
    return render(request, 'core/gold.html')


@login_required
def silver(request):
    return render(request, 'core/silver.html')


@login_required
def contact(request):
    return render(request, 'core/contact.html')


def logout_view(request):
    response = redirect('/thank-you/')  # Redirect to thank you page
    response.set_cookie('logged_out', 'true', max_age=settings.LOG_OUT_COOKIE_DURATION)
    logout(request)
    return response


def thank_you(request):
    return render(request, 'core/thank_you.html')


def search_view(request):
    return HttpResponse('Rate limit exceeded', status=429)