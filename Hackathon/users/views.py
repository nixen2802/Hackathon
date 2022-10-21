from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Congrats {username}!!')
            return redirect('Home page')
    else:
        form=UserRegisterForm()
    form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

def login(request):
    if request.method=="POST":
        return render(request, 'users/login.html')
    return render(request, 'users/register.html')
