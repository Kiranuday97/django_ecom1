from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

		widgets={
            "username":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            "email":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            "password1":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            "password2":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            
        }

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user