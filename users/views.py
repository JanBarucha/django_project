import string

from django.shortcuts import render, redirect
import secrets
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def generate_password(request):
    form = UserRegisterForm(request.POST)

    letters = string.ascii_letters
    spec_chars = string.punctuation
    digits = string.digits

    input_for_genrator = letters + spec_chars + digits
    pass_lenght = 8

    pass_word = ''
    for _ in range(pass_lenght):
        pass_word += ''.join(secrets.choice(input_for_genrator))

    context = {
        'form' : form,
        'genPass' : pass_word
    }

    return render(request, 'users/GeneratorPage.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your accout has been created ! Try to log in  {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your accout has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)
