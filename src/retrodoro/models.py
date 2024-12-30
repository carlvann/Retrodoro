from django.db import models

# Create your models here.
class Users(models.Model):
    uuid = models.CharField(max_length=32)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=32)
    creation_date = models.DateTimeField("date created")


class Tasks(models.Model):
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    session_length = models.DurationField()
    date_completed = models.DateTimeField("date completed")
