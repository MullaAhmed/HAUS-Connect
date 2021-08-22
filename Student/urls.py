from django.urls import  path
from . import views

urlpatterns = [
    path("student_home/",views.home,name="Home"),
    path("chatbot/",views.chatbot,name="ChatBot"),
    path("FAQ/",views.faq,name="FAQ"),
    path("Result/",views.result,name="Result"),
    path("TimeTable/",views.timetable,name="TimeTable"),
    path("logout/",views.logout_request,name="logout"),
    path("about/",views.about,name="About")

    
    
]