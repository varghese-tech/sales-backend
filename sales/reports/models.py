from http.client import PRECONDITION_REQUIRED
from django.db import models

# Create your models here.

class Agents(models.Model):
    AgentId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Hired = models.DateField()
    Birthday = models.DateField()
    City = models.CharField(max_length=100)

class Reports(models.Model):
    ReportId = models.AutoField(primary_key=True)
    AgentId = models.ForeignKey(Agents, to_field="AgentId", on_delete=models.CASCADE)
    Period = models.CharField(max_length=100)
    Volume = models.FloatField()
