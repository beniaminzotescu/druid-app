from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'core/index.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login')  # Redirect to a success page.
