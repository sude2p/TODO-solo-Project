from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserLogin(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        
    #------for password functionality-------#    
    def __init__(self, *args, **kwargs):
        super(UserLogin, self).__init__(*args, **kwargs)

        # Set the password field widget to PasswordInput
        self.fields['password'].widget = forms.PasswordInput()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2'] 