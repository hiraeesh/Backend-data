from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.
class UserData(models.Model):
    id=models.IntegerField(primary_key=True)
    Em_name=models.CharField(max_length=40)
    Em_company_name=models.CharField(max_length=40)
    Em_Sallary=models.IntegerField()