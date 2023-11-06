import logging

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


def save_group(sender, instance, created, **kwargs):
    p = Partner.objects.filter(user=instance)
    if not p:
        Partner.objects.create(user=instance)


post_save.connect(save_group, sender=User)
