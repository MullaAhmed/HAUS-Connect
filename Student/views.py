

from Teacher.models import Announcements,Exam,Class
from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def home(response):
    t1=Announcements.objects.all()
    t2=Class.objects.all()
    t3=Exam.objects.all()
    return render(response,"Student/student_home.html",{"t1":t1,"t2":t2,"t3":t3})

def chatbot(response):
    return render(response,"Student/ChatBot.html")

#def notes(response):
#   return render(response,"Student/student_home.html")

def timetable(response):
    return render(response,"Student/TimeTable.html")

def result(response):
    return render(response,"Student/Result.html")

#def about(response):
 #   return render(response,"Student/student_home.html")

def faq(response):
    return render(response,"Student/faq.html")

def logout_request(request):
    logout(request)
    return render(request,"Student/student_home.html",{})  

def about(request):
    return render(request,"Student/About.html",{})

