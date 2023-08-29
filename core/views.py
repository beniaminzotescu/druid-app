from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'core/index.html')


def logout_view(request):
    logout(request)
    return render(request, 'core/logout.html')  # Redirect to a success page.
