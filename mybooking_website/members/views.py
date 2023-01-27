from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.warning(request, ('There was an error logging in, try again'))
			return redirect('login')
	else:
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return render(request, 'registration/login.html')

def logout_user(request):
	logout(request)
	messages.success(request, ('You have successfully logged out'))
	return redirect('home')

def register_user(request):
	if request.method == "POST":
		# get the form class from django.contrib.auth.forms 
		# and feed it the inputted user data
		form = RegisterUserForm(request.POST)

		# if the form check was valid
		if form.is_valid():
			# save the form data
			form.save()

			# sanitize the data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']

			# authenticate the user
			user = authenticate(username=username, password=password)

			# login the user
			login(request, user)

			# flash message
			messages.success(request, ('Registration successful!'))

			# redirect to 'home'
			return redirect('home')
	else:
		if request.user.is_authenticated:
			return redirect('home')
		else:
			form = RegisterUserForm()
			return render(request, 'registration/register_user.html', {'form': form})