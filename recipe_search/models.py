from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# This model is for the saved list of ingredients
# TODO 1 FIX MODEL FOR ADDING TO DB
class SavedList(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	saved_list = models.TextField(verbose_name="savedlist")

	def __str__(self):
		return f'{self.user.username} List'