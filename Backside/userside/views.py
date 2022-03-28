from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from .models import UserData 

class Userdataa(ListView):
     model = UserData
     template_name = 'student/node.html'
     context_object_name = 'student'

