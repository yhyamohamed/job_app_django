from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import User


@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    user = kwargs.get('instance')
    if user.user_type == 'recruiter':
        # send_mail('new recruiter has beenn added ')
        send_mail(
            'new recruiter has been added ',  # subject
            user.email + ' has been created ',  # message
            'system@admin.com',  # from
            ['admin@admin.com'],  # to
        )
