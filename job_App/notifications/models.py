from django.db import models


class Notification(models.Model):
    name = models.CharField(max_length=30)
    modification_time = models.DateField(auto_now=True)
