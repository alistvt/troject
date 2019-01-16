from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'group', 'status')
    search_fields = ('user', 'group', 'status', 'created', 'ip', 'country')

admin.site.register(Task, TaskAdmin)
