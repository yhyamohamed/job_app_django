from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Job


@receiver(post_save, sender=Job)
def send_notification_on_job_create(sender, instance, created, **kwargs):
    if created:
        print('test')
