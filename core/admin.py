from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'has_logged_in')  # Display these fields in the list view
    list_filter = ('has_logged_in',)  # Add a filter for the has_logged_in field


admin.site.register(UserProfile, UserProfileAdmin)
