from django.shortcuts import render
from . import forms
from Myapp.forms import NewUserForm, UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'Myapp/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request, 'Myapp/registration.html', {'user_form':user_form,'profile_form':profile_form, 'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username:{} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'Myapp/login.html')

def users(request):
    form=NewUserForm()
    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'user.html', {'form':form})

def form_name_view(request):
    form=forms.FormName()

    if request.method == 'POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request, 'form_page.html', {'form':form})

def other(request):
    return render(request, 'other.html')

def relative(request):
    return render(request, 'relative_url_templates.html')
