import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.timezone import utc
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from datetime import datetime
from .models import Task
from .forms import LoginForm, TaskForm
from .helper_functions import getTasksCategorized

logger = logging.getLogger(__name__)

# Create your views here.

def loginUser(request):
	if request.user.is_authenticated:
		return redirect(reverse('tasks:home'))

	elif request.method == 'GET':
		return render(request, 'login.html')

	elif request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'].lower(),password=cd['password'])
			if user is not None:
				login(request, user)
				return redirect(reverse('tasks:home'))
			else:
				return render(request, 'login.html', {'error':'Username and password doesn\'t match.'})

def logoutUser(request):
	if request.user.is_authenticated:
		logout(request)
	return redirect(reverse('tasks:login'))

@login_required
def home(request):
	user = request.user
	groups = Task.Groups.choices
	if user.is_superuser:
		tasks = getTasksCategorized(tasks=Task.objects.all().order_by('-createdDate'))
		users = User.objects.all()
		context={'tasks':tasks, 'users':users, 'groups':groups, 'colors':Task.Groups.colors}
	else:
		tasks = getTasksCategorized(tasks=Task.objects.filter(user=user))
		context={'tasks':tasks, 'groups':groups, 'colors':Task.Groups.colors}
	context['messages']= messages.get_messages(request)
	return render(request, 'home.html', context)

@login_required
def addTask(request):
	# superuser check
	if not request.user.is_superuser:
		messages.error(request, 'Sorry! You don\'t have permission to do this!')
		return redirect(reverse('tasks:home'))

	if request.method == 'POST':
		task = TaskForm(request.POST)
		if task.is_valid():
			task = task.save()
			messages.success(request, 'Task added successfuly!')
			return redirect('tasks:home')
		else:
			logger.debug('errors in form.')
			messages.error(request, 'Sorry! Some errors happened!')
	else:
		messages.error(request, 'Method GET unsupported!')
		return redirect(reverse('tasks:home'))
		# NOTE:
		# 404

@login_required
def doneTask(request, id):
	user = request.user
	task = get_object_or_404(Task, id=id)
	if user==task.user or request.user.is_superuser:
		task.status = Task.Statuses.done
		task.doneDate = datetime.utcnow().replace(tzinfo=utc)
		task.save()
		messages.success(request, 'Task status changed to done successfuly!')
		return redirect(reverse('tasks:home'))

	# NOTE: inja bege to dastesi nadari or 404
	messages.error(request, 'Sorry! Some errors happened!')
	return redirect(reverse('tasks:home'))

@login_required
def deleteTask(request, id):
	if request.user.is_superuser:
		task = get_object_or_404(Task, id=id)
		task.delete()
		messages.success(request, 'Task deleted successfuly!')
		return redirect(reverse('tasks:home'))
	else:
		messages.error(request, 'Sorry! You don\'t have permission to do this!')
		return redirect(reverse('tasks:home'))
