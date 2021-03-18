from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, Create_Services

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Si tu captes pas go look ça https://www.youtube.com/watch?v=tUqUdu0Sjyc

from .models import Services_Users

# var glob
user = ""

# Create your views here.
def register(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Bravo, ton compte à été créer avec succès!")
			return redirect('login')

	context = {'form': form}
	return render(request, 'login/register.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get("username")
		password =request.POST.get("password")
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Le nom d'utilisateur ou le mot de passe est incorrect...")
	context = {}
	return render(request, 'login/login.html', context)

@login_required(login_url="home")
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url="login")
def profile_page(request):
	context = {'user':  request.user}
	return render(request, 'profile_app/profile.html', context)

@login_required(login_url="login")
def services_page(request):
	username = request.user
	form = Create_Services()
	if request.method == 'POST':
		form = Create_Services(request.POST)
		if form.is_valid():
			return print('ça marche')
	context = {'user':  request.user, 'form': form}
	return render(request, 'services/services.html', context) # TODO: Finir le systeme de création de services