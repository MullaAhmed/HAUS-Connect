from django.urls import  path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("<int:id>",views.index,name="index"),
    path("announcement/",views.create_announcement,name="Announcement"),
    path("class/",views.create_class,name="Extra Class"),
    path("exam/",views.create_exam,name="Exams"),
    path("logout/",views.logout_request,name="logout"),
    path("base/",views.base,name="Base"),

    
]