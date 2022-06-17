from django.db import models

from accounts.models import User


class Notification(models.Model):
    name = models.CharField(max_length=30)
    modification_time = models.DateField(auto_now=True)
    sent_to = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='receiver')

    def __str__(self):
        return self.name
