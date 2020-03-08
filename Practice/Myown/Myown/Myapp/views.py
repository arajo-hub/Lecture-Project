from django.shortcuts import render
from . import forms
from Myapp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

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
