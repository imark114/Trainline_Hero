from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id': 'required'}))
    nid = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'nid', 'password1', 'password2']
    
    def save(self):
        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        nid = self.cleaned_data.get('nid')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        account = User(username=username, first_name=first_name, last_name=last_name, email=email, nid=nid)
        account.set_password(password1)
        account.is_active = False
        account.save()
        return account

class UpdateProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields= ['first_name', 'last_name', 'email', 'nid']