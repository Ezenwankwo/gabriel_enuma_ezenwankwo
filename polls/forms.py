from django import forms
from django.forms import ModelForm
from .models import Profile


class ProfileForm(forms.ModelForm):
	class Meta:
		model 	= Profile
		exclude = ['user', 'created', 'updated', 'slug']