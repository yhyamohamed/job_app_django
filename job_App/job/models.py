from django.contrib.auth.models import AbstractUser
from django.db import models

# from job_App.accounts.models import Tag, User
from accounts.models import User, Tag


class Job(models.Model):
    STATUS = (
        ('open', 'open'),
        ('in_progress', 'in_progress'),
        ('ﬁnished', 'ﬁnished'),
    )
    name = models.CharField(max_length=30)
    creation_time = models.DateField(auto_now_add=True)
    modification_time = models.DateField(auto_now=True)
    description = models.TextField(max_length=255)
    tags = models.ManyToManyField('accounts.Tag')
    applied_developers = models.ManyToManyField('accounts.User', blank=True)
    developer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='developer')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    status = models.fields.CharField(choices=STATUS, max_length=11, default='open')
