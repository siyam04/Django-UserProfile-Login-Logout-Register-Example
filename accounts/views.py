from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
    PasswordChangeForm
)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)

from .models import UserProfile


@login_required
def login(request):
    return render(request, 'accounts/login.html')


@login_required
def logout(request):
    return render(request, 'accounts/logout.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/view-profile/')
    else:
        form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': request.user}
    return render(request, 'accounts/view_profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'accounts/change_password.html', {'form': form})
