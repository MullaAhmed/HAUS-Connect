from datetime import date
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from .decorator import allowed_users

from .models import *
from .forms import *
from .Sending_messages import *
# Create your views here.
def base(request):
    return render(request,"base.html")

@allowed_users(allowed_roles=['admin','Professor'])
def home(response):
    return render(response,"home.html")

def logout_request(request):
    logout(request)
    return render(request,"home.html",{})

@allowed_users(allowed_roles=['admin','Professor'])
def index(response,id):
    a=Announcements.objects.get(id=id)
    return render(response,"home.html",{})

@allowed_users(allowed_roles=['admin','Professor'])
def create_announcement(response):
    if response.method == "POST":
        form=createnewannouncement(response.POST)

        if form.is_valid():
            t=form.cleaned_data["text"]
            a=Announcements(text=t)
            a.save()
            
            if form.cleaned_data["check"]==True:
                send_message(t)
                messages.success(response,'Announcement was saved and messages are sent')
            else:
                messages.success(response,'Announcement was saved')
            return render(response,"home.html",{})
    else:
        form=createnewannouncement()
        return render(response,"announcement.html",{"form":form})

@allowed_users(allowed_roles=['admin','Professor'])
def create_class(response):
    if response.method == "POST":
        form=schedule_extra_class(response.POST)

        if form.is_valid():
            c1=form.cleaned_data["subject"]
            c2=form.cleaned_data["date"]
            c3=form.cleaned_data["time_start"]
            c4=form.cleaned_data["time_end"]
            c=Class(subject=c1,date=c2,time_start=c3,time_end=c4)
            c.save()
            t="You have a {0} extra class on {1} from {2} to {3}".format(str(c1),str(c2),str(c3),str(c4))
            if form.cleaned_data["check"]==True:
                send_message(t)
                messages.success(response,'Class is scheduled and messages are sent')
            else:
                 messages.success(response,'Class is scheduled')
            return render(response,"home.html",{"text":t})
    else:
        form=schedule_extra_class()
        return render(response,"class.html",{"form":form})

@allowed_users(allowed_roles=['admin','Professor'])    
def create_exam(response):
    if response.method == "POST":
        form=schedule_exam(response.POST)

        if form.is_valid():
            e1=form.cleaned_data["subject"]
            e2=form.cleaned_data["date"]
            e3=form.cleaned_data["time_start"]
            e4=form.cleaned_data["time_end"]
            e=Exam(subject=e1,date=e2,time_start=e3,time_end=e4)
            e.save()
            t="You have a {0} exam on {1} from {2} to {3}".format(str(e1),str(e2),str(e3),str(e4))

            if form.cleaned_data["check"]==True:
                send_message(t)
                messages.success(response,'Exam is scheduled and messages are sent')
            else:
                 messages.success(response,'Exam is scheduled')
                 
            return render(response,"home.html",{"text":t})
    else:
        form=schedule_exam()
        return render(response,"exam.html",{"form":form})

#alert
