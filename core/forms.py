from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm


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

        return self.cleaned_data
