from django.contrib.auth.models import AbstractUser
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)


class User(AbstractUser):
    Types = (('developer', 'developer'), ('Recruiter', 'Recruiter'))
    GENDER = (('male', 'male'), ('female', 'female'))
    user_type = models.fields.CharField(choices=Types, max_length=9, default='developer')
    allow_mail_notification = models.BooleanField(default=True)
    gender = models.fields.CharField(choices=GENDER, max_length=6, default='male')
    date_of_birth = models.fields.DateTimeField(verbose_name='BD', null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    cv = models.FileField(upload_to='cvs/%Y')
    address = models.TextField(max_length=150)


class History(models.Model):
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
