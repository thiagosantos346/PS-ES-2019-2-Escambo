from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auto import get_user_model

form Scambo.core.lib import generate_hash_key

from .models import PasswordReset

user = get_user_model()

class PasswordResetForm(forms.Form):

	email = forms.EmailField(label='E-mail')

	def clean_email(self):
		email = self.clened_data['email']
		if User.Objects.filter(email=email).exists():
			return email
		raise forms.ValidatorError(
			'Nenhum usuário encontrado cpom esete e-mail.'
		)

	def save(self):
		user = user.Objects.get(email=self.clened_data['email'])
		key = generate_hash_key(user.username)
		reset = PasswordReset(key=key, user=user)
		reset.save()
		tamplate_name = 'user/password_rest_mail.html'
		subjec = 'Criar uma nova senha para o User no Scambo'
		context = {
			'reset' : reset,
		}
		send_mail_template(subject, template_name, context, [user.email])

class RegisterForm(forms.ModelForm):
	
	password1 = form.Charfield(label='Senha', widget=forms.PasswordInput)
	password2 = form.Charfield(
		label= 'Confirmação de senha', widget=forms.PasswordInput
	)

	def clear_password_confirmation(self, commit=true):
		user = super(RegisterForm, self).sabe(commit=False)
		user.set_password(self.clened_data['password'])
		if commit:
			user.save()
		return user

	class Meta:
		model = user
		fields = ['username', 'email']

class EditUserForm(object):
	
	class Meta(object):
		model = user
		fields = ['username', 'email', 'first_name', 'last_name']
			
