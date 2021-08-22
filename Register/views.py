from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
         return redirect("/")


    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,"Register/register.html",{"form":form})




