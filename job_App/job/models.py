from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

# from job_App.accounts.models import Tag, User
from accounts.models import User, Tag
from django.core.mail import send_mail


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
        users = User.objects.filter(tags__in=tags).distinct()
        for user in users:
            print(user.email)
            send_mail('New Job Has Been Posted', 'New Job!', 'admin@admin.com', [user.email], fail_silently=False)


@receiver(post_save, sender=Job)
def send_notification_on_job_accept(sender, instance, update_fields, **kwargs):
    if list(update_fields)[0] == 'developer_id':
        accepted_mail = User.objects.get(pk=instance.developer_id).email
        print(accepted_mail)
        send_mail('You Have Been Accepted', 'New Job!', 'admin@admin.com', [accepted_mail], fail_silently=False)

        rejected_developers = instance.applied_developers.exclude(email=accepted_mail)
        for developer in rejected_developers:
            print(developer.email)
            send_mail('Sorry, You Have Been Rejected', 'New Job!', 'admin@admin.com', [developer.email],
                      fail_silently=False)

    elif list(update_fields)[0] == 'status':
        job_owner_mail = User.objects.get(pk=instance.created_by_id).email
        print(job_owner_mail)
        send_mail('Job has been posted', 'New Job!', 'admin@admin.com', [job_owner_mail], fail_silently=False)
