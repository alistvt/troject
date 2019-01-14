import logging
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from .helper_functions import getTasksCategorized
from .models import Task
from .forms import LoginForm, TaskForm
from datetime import datetime
from django.utils.timezone import utc

logger = logging.getLogger(__name__)

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
		context={'tasks':tasks, 'users':users, 'groups':groups, 'colors':Task.Groups.colors}
	else:
		tasks = categorizeTasks(tasks=Task.objects.filter(user=user))
		context={'tasks':tasks, 'groups':groups, 'colors':Task.Groups.colors}
	return render(request, template_name='home.html', context=context)

# superuser check
def addTask(request):
	print('hehheheheheheheheh')
	if request.method == 'POST':
		print(request.POST)
		task = TaskForm(request.POST)
		print(task)
		if task.is_valid():
			task = task.save()
			print(task)
			return redirect(reverse('tasks:home'))
		else:
			logger.debug(form.errors)
			print(form.errors)
			# print(form.errors)
	else:
		return redirect(reverse('tasks:home'))
		# NOTE:
		# 404

def doneTask(request, id):
	user = request.user
	task = get_object_or_404(Task, id=id)
	if user==task.user or request.user.is_superuser:
		task.status = Task.Statuses.done
		task.doneDate = datetime.utcnow().replace(tzinfo=utc)
		task.save()
		return redirect(reverse('tasks:home'))

	# NOTE: inja bege to dastesi nadari or 404
	return redirect(reverse('tasks:home'))

# if request.user.is_superuser:
def deleteTask(request, id):
	task = get_object_or_404(Task, id=id)
	task.delete()
	return redirect(reverse('tasks:home'))
