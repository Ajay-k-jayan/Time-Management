from django.db import models

# Create your models here.

# tasks model
class Task(models.Model):
    TaskId = models.AutoField(primary_key=True)
    TaskName = models.CharField(max_length=200)
    Status = models.CharField(max_length=100)
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    CreatedDate = models.DateField()
    ApprovalStatus = models.CharField(max_length=100)
    AssignedManager = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)

