from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Calculator


@receiver(post_save, sender=Calculator)
def create_user_profile(sender, created, **kwargs):
    if created:
        print("action created!")
