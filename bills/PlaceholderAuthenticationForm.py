from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput
from django.forms.fields import CharField

class PlaceholderAuthenticationForm(AuthenticationForm):
    """ Extend AuthenticationForm with placeholder attr for form fields"""
    
    username = CharField(label="Username", max_length=30, 
                         widget=TextInput(attrs={'placeholder' : 'Username'}))
    password = CharField(label="Password", 
                         widget=PasswordInput(attrs={'placeholder' : 'Password'}))
