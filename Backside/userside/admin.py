from django.contrib import admin
from .models import UserData
# Register your models here.

@admin.register(UserData)
class Studentadmin(admin.ModelAdmin):
    list_display=['id','Em_name','Em_company_name','Em_Sallary'] 
