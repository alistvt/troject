from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import LoginForm
from .helper_functions import getTasksCategorized
from .models import Task
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
	groups = Task.Groups.choices
	if user.is_superuser:
		tasks = getTasksCategorized(tasks=Task.objects.all())
		users = User.objects.all()
		return render(request, template_name='home.html', context={'tasks':tasks, 'users':users, 'groups':groups})
	else:
		tasks = categorizeTasks(tasks=Task.objects.filter(user=user))
		return render(request, template_name='home.html', context={'tasks':tasks, 'groups':groups})

# superuser check
def addTask(request):
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid:
			task = form.save()
	else:
		pass
		# 404
