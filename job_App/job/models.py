from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

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
    tags = models.ManyToManyField('accounts.Tag', blank=True)
    applied_developers = models.ManyToManyField('accounts.User', blank=True)
    developer = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='developer')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    status = models.fields.CharField(choices=STATUS, max_length=11, default='open')


@receiver(m2m_changed, sender=Job.tags.through)
def send_notification_on_job_create(sender, instance, **kwargs):
    if kwargs.get('action') == 'post_add' and ContentType.objects.get_for_model(sender).name == 'job-tag relationship':
        tags = instance.tags.all()
        users = User.objects.filter(tags__in=tags)
        for user in users:
            print(user.email)

