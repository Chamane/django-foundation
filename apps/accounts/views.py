from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, get_user_model
from django.urls import reverse

from .forms import LoginForm, RegisterForm

def login(request):
    # if request is a HTTP POST try to pull out the relevant information
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            #if user is not None:
                #auth_login(request, user)
                #if user.is_activate:
                    #return redirect('doctor_dashboard', user_slug=user.slug)
                #else:
                    #return redirect(reverse('home'))

    else:
        login_form = LoginForm()

    return render(request, 'accounts/login.html', {'login_form': login_form,})


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid(): # TODO: add recaptcha validation
            user = register_form.save()
            auth_login(request, user)
            return redirect(reverse('home'))
    else:
        register_form = RegisterForm()

    return render(
        request, 'accounts/register.html',
        {'register_form': register_form}
    )
