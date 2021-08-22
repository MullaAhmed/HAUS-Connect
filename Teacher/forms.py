from django import forms

class createnewannouncement(forms.Form):
    text=forms.CharField(label="Announcement",max_length=1000)
    check=forms.BooleanField(label="Send message",required=False)


class schedule_extra_class(forms.Form):
    subject=forms.CharField(label="Subject",max_length=20)
    date=forms.CharField(label="Date",max_length=20)
    time_start=forms.CharField(label="Starting Time",max_length=20)
    time_end=forms.CharField(label="Ending Time",max_length=20)
    check=forms.BooleanField(label="Send message",required=False)

class schedule_exam(forms.Form):
    subject=forms.CharField(label="Subject ",max_length=20)
    date=forms.CharField(label="Date",max_length=20)
    time_start=forms.CharField(label="Starting Time",max_length=20)
    time_end=forms.CharField(label="Ending Time",max_length=20)
    check=forms.BooleanField(label="Send message",required=False)