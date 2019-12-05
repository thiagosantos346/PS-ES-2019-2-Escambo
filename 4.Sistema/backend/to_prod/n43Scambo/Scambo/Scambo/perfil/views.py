from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, SetPasswordForm)
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from .models import User, UserAvatar

user = get_user_model()

@login_required
def dashBoard(request):
	template_name = 'dashBoard.html'
	context = {}
	return render(request, template_name, context)

def register(request):
	template_name = 'register.html'
	if request.method == 'POST':
		form = registerForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = authenticate(
				username=user.username, password=form.clened_data['password1']
			)
			login(request, user)
			return redirect('core:home')
		else:
			form = registerForm(request, user)
		context = {
			'form': form
		}

		return render(request, template_name, context)

def password_reset(request):
	template_name = 'password_reset_confirm.html'
	context = {}
	reset = get_object_or_404(passwordReset, key=key)
	Form = SetPasswordForm(user=reset.user, data=request.POST or None)
	if form.is_valid():
		form.save()
		context['successe'] = True
	context['form'] = form
	return render(request, template_name, context)

@login_required
def edit(request):
	template_name = 'edit.html'
	context = {}
	if request.method == 'POST':
		form = EditUserForm(request.POST, instance=request.user )
		if form.is_valid():
			form.save()
			messages.success(
				request, 'Os dados do seu user foram alterados com sucesso.'
			)
			return redirect('perfil:dashBoard')
	else:
		form = EditUserForm(instance=request.user)
	context['form'] = form

	return render(request, template_name, context)

@login_required
def edit_password(request):
    template_name = 'edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)