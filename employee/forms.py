from django import forms
from .models import emp
from django.contrib.auth.models import User

class empForm(forms.ModelForm):
	class Meta:
		model=emp
		fields='__all__'
		

class updateForm(forms.ModelForm):
	class Meta:
		model=emp
		fields='__all__'
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

