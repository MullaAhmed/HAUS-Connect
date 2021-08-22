from django.db import models

# Create your models here.
class Announcements(models.Model):
    text=models.TextField(max_length=500)
    def __str__(self):
        return self.text

class Class(models.Model):
    subject=models.TextField(max_length=50)
    date=models.TextField(max_length=50)
    time_start=models.TextField(max_length=5)
    time_end = models.TextField(max_length=5)
    message="You have a {0} extra class on {1} from {2} to {3}".format(str(subject),str(date),str(time_start),str(time_end))
    def __str__(self):
        message="You have a {0} extra class on {1} from {2} to {3}".format(str(self.subject),str(self.date),str(self.time_start),str(self.time_end))
        return self.message

class Exam(models.Model):
    subject=models.TextField(max_length=50)
    date=models.TextField(max_length=50)
    time_start=models.TextField(max_length=5)
    time_end = models.TextField(max_length=5)
    message="You have a {0} exam on {1} from {2} to {3}".format(str(subject),str(date),str(time_start),str(time_end))
    def __str__(self):
        message="You have a {0} exam on {1} from {2} to {3}".format(str(self.subject),str(self.date),str(self.time_start),str(self.time_end))
        return self.message