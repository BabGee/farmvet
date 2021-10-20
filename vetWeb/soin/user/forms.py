from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()

class VetOfficerSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
		
	email = forms.EmailField(
		max_length=254,
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'Email',
				'class': 'form-control'
			}
		)
	)
	phone_number = forms.RegexField(regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', max_length=13)
	kvb_number = forms.CharField()
	
	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'form-control'
			}
		)
	)

	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'form-control'
			}
		)
	)
	
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','first_name','last_name','kvb_number','phone_number','email','password1', 'password2',)

	
class FarmerSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=50,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
	email = forms.EmailField()
	phone_number = forms.RegexField(regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', max_length=13)
	farm_name  = forms.CharField(max_length=20)
	location = forms.CharField(max_length=30)
	password1 = forms.CharField(
		label='Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'form-control'
			}
		)
	)

	password2 = forms.CharField(
		label='Confirm Password',
		max_length=30,
		min_length=8,
		required=True,
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'form-control'
			}
		)
	)


	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username','first_name','last_name','farm_name','email', 'location','password1', 'password2']
			

class StudentSignUpForm(UserCreationForm):
	first_name = forms.CharField(
		max_length=10,
		min_length=4,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'First Name',
					'class': 'form-control'
				}
			)
		)
	last_name = forms.CharField(
		max_length=30,
		required=True,
		widget=forms.TextInput(
				attrs={
					'placeholder': 'Last Name',
					'class': 'form-control'
				}
			)
		)
	email = forms.EmailField()
	phone_number = forms.RegexField(regex='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', max_length=13)
	student_number = forms.CharField(max_length=20)
	college_name = forms.CharField(max_length=20)
	location = forms.CharField(max_length=30)

	class Meta(UserCreationForm.Meta):
		model = User
		fields = ['username','first_name','last_name','student_number','college_name', 'phone_number', 'email', 'location','password1', 'password2']	
