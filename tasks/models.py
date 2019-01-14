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
        idea = 0
        research = 1
        strategy = 2
        performance = 3
        bugs = 4
        buy = 5
        choices = (
            (idea, 'Idea'),
            (research, 'Research'),
            (strategy, 'Strategy'),
            (performance, 'Performance'),
            (bugs, 'Bugs'),
            (buy, 'Buy'),
        )

        # each coler is related to its index value in groups
        colors = [
            '#8f7ee6',
            '#ff9f1a',
            '#ffd500',
            '#8acc47',
            '#d93651',
            '#00aaff',
        ]

    class Statuses:
        done = True
        pending = False

    title = models.CharField(max_length=255)
    status = models.BooleanField(default=Statuses.pending)
    group = models.PositiveSmallIntegerField(choices=Groups.choices, default=Groups.idea)
    user = models.ForeignKey(User, related_name='tasks', blank=True, null=True, on_delete=models.SET_NULL)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    doneDate = models.DateTimeField(blank=True, null=True)
