from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from recipe_search.models import SavedList

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


# class SavedListForm(forms.ModelForm):
#     class Meta:
#         model = SavedList
#         fields = ('saved_list',)
    
