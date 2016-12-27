from django.db import models

class Programmer(models.Model):

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=50)
    jobExperience = models.FloatField()
    salary = models.IntegerField()
    progLang = models.CharField(max_length=50)
    file = models.FileField(upload_to='downloads/')


    def dic(self):
        return {'name': self.name,
                'surname': self.surname,
                'birthdate': self.birthdate,
                'jobExperience': self.jobExperience,
                'salary': self.salary,
                'progLang': self.progLang,
                'file': self.file.name}