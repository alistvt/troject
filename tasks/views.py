from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .helper_functions import getTasksCategorized
# Create your views here.

def loginUser(request):
	if request.user.is_authenticated:
		return redirect(reverse('tasks:home'))

	elif request.method == 'GET':
		pass

	elif request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['email'].lower(),password=cd['password'])
			if user is not None:
				login(request, user)
				return redirect(reverse('tasks:home'))
			else:
				errors = ('ایمیل و یا پسورد شما اشتباه است. لطفا دوباره تلاش کنید.','Username and password doesn\'t match.')[lan]
				messages.error(request, errors)
				return render(request,('fa/banners/login.html','en/banners/login.html')[lan], { 'lastads': lastads})

def logoutUser(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect(reverse('tasks:login'))

def home(request):
	user = request.user
	if user.is_superuser:
		tasks = categorizeTasks(tasks=Task.objects.all())
	else:
		tasks = categorizeTasks(tasks=Task.objects.filter(user=user))
	return render(request, 'home.html', {'tasks':tasks})
