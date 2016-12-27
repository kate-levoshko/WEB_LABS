from django.contrib import admin
from .models import Programmer

class ProgrammerAdmin(admin.ModelAdmin):
    fields = ['name' , 'surname', 'birthdate' , 'jobExperience', 'salary' , 'progLang', 'file']

admin.site.register(Programmer , ProgrammerAdmin)


