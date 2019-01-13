from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as authViews

app_name='tasks'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
]