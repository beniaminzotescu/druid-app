from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import redirect


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if hasattr(request, 'session') and not request.user.is_anonymous:
            last_activity_str = request.session.get('last_activity')
            if last_activity_str:
                last_activity = datetime.strptime(last_activity_str, '%Y-%m-%d %H:%M:%S.%f')  # Convert back to datetime
                elapsed_time = datetime.now() - last_activity
                if elapsed_time.total_seconds() > settings.SESSION_EXPIRE_SECONDS:
                    # Clear user session and log them out
                    request.session.flush()
                    return redirect('/logout')  # Redirect to logout page or appropriate URL

        # Update last activity timestamp
        request.session['last_activity'] = str(datetime.now())  # Convert datetime to string

        return response
