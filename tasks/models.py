import logging
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

logger = logging.getLogger(__name__)

# class Group(models.Model):
#     """In case needed to add groups:
#        Model which keeps groups. each group is related to a Task instance."""
#

class Task(models.Model):
    """
    Model which keeps tasks.
    each Task record has:
    `title`,
    `status: False if for pending and True is for done
    `group`: is an IntegerField which have is a choice of the class `Groups`
    """
    class Groups:
        """Class containing Todo groups"""
        ungrouped = 0
        group1 = 1
        group2 = 2
        group3 = 3
        choices = ((ungrouped, 'Ungrouped'),
        (group1, 'Group 1'),
        (group2, 'Group 2'),
        (group3, 'Group 3'),)

    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    group = models.PositiveSmallIntegerField(choices=Groups.choices, default=Groups.ungrouped)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    done = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, related_name='tasks', blank=True, null=True,on_delete=models.SET_NULL)
