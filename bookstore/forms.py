from django import forms
from django.contrib.auth import (authenticate, get_user_model )
from .models import Author
User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError('This user does not exist')
			if not user.check_password(password):
				raise forms.ValidationError('Incorrect password')

			if not user.is_active:
				raise forms.ValidationError('This user is not active')
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Email address')
	email2 = forms.EmailField(label='Confirm email')
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = [
			'username', 
			'email', 
			'email2', 
			'password'
		]

	def clean(self, *args, **kwargs):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError('emails are not same')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError('this email is already being used')
		return super(UserRegisterForm, self).clean(*args, **kwargs)

class SearchForm(forms.ModelForm):
	# query = forms.CharField()
	class Meta:
		model = Author
		fields = ('firstname',)

	def clean(self, *args, **kwargs):
		raw_query= self.cleaned_data.get('firstname').strip()
		firstname, lastname = raw_query[0], raw_query[1]
		check = Author.objects.filter(firstname=raw_query)
		if check.exists():
			return super(SearchForm, self).clean(*args, **kwargs)





