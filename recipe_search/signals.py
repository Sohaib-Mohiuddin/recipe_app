from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# from .models import SavedList

# def create_list(sender, instance, created, **kwargs):
# 	if created:
# 		SavedList.objects.create(user=instance)

# def update_list(sender, instance, **kwargs):
# 	instance.