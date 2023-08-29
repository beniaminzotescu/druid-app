from datetime import datetime
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not request.user.is_authenticated:  # Simplified check for anonymous user
            if request.COOKIES.get('logged_out'):
                if request.path != reverse('core:thank_you'):
                    return redirect('core:thank_you')  # Redirect to thank you page

        if hasattr(request, 'session') and not request.user.is_anonymous:
            login_time_str = request.session.get('login_time')
            if login_time_str:
                login_time = datetime.strptime(login_time_str, '%Y-%m-%d %H:%M:%S.%f')
                elapsed_time = datetime.now() - login_time
                if elapsed_time.total_seconds() > settings.SESSION_EXPIRE_SECONDS:
                    # Clear user session and log them out
                    request.session.flush()
                    response = redirect('/logout')  # Redirect to logout page or appropriate URL

            # Update login time only if not already set
            if not login_time_str:
                request.session['login_time'] = str(datetime.now())

        return response
