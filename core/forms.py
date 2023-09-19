from datetime import datetime, timedelta

from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .models import UserProfile


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Adresă de email*',
        'class': 'form-control'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Parolă*',
        'class': 'form-control'
    }))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    'Invalid username or password. Please try again.', code='invalid_login'
                )
            else:
                self.confirm_login_allowed(self.user_cache)

                # Get the UserProfile instance for the user
                user_profile, created = UserProfile.objects.get_or_create(user=self.user_cache)

                if user_profile.has_logged_in:
                    raise forms.ValidationError(
                        'You are already logged in. Only one login attempt is allowed.',
                        code='already_logged_in'
                    )
                user_profile.last_login_datetime = datetime.now()
                user_profile.has_logged_in = True
                user_profile.save()

        return self.cleaned_data


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Name*',
            'class': 'form-control'
        }),
        max_length=30,
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email*',
            'class': 'form-control'
        }),
        max_length=100,
    )

    phone = forms.CharField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Phone',
            'class': 'form-control'
        }),
        max_length=20,
        required=False,  # Phone field is optional
    )

    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Message*',
            'class': 'form-control'
        }),
        max_length=1000,
    )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone = int(phone)
        # Check if phone is a string
        if not isinstance(phone, str):
            raise ValidationError("Phone number must be a string.")

        # You can add additional phone number validation logic here

        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        # You can add custom email validation logic here
        # if not email.endswith('@testin.com'):  # Replace with your validation rule
        #     raise ValidationError("Invalid email address. Please use a valid domain.")
        if email is not int:
            raise ValidationError("Invalid email address. Email should be int.")
        return email

    def clean_message(self):
        message = self.cleaned_data['message']
        # You can add custom message validation logic here
        if len(message) < 10:
            raise ValidationError("Message should be at least 30 characters long.")
        return message
