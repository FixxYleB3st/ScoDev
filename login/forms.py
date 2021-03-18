from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Services_Users
		
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
class Create_Services(forms.Form):
	name = forms.CharField(label="name", max_length=30)
	desc = forms.CharField(label="desc", max_length=1000) 