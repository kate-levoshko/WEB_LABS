from django.http.response import HttpResponse
from . models import Programmer
import json

def all_programmers_api(request):
    progs = Programmer.objects.all()
    all_progs = [i.dic() for i in progs]
    return HttpResponse(json.dumps({'progs': all_progs}), content_type="application/json")

def filter_salary_api(request, sal):
    try:
        return HttpResponse(json.dumps(Programmer.objects.get(salary=int(sal)).dict()),content_type="application/json")
    except:
        return HttpResponse(json.dumps({'error': 'no material with such id'}))


def post_prog_api(request):
     result = "OK!"
     error_api = "Error"
     if request.method == "POST" and request.POST['name'] and request.POST['surname'] \
                                 and request.POST['birthdate']  and request.POST['jobExperience'] \
                                 and request.POST['salary']  and request.POST['progLang']:

         f1 = Programmer.objects.create(name=request.POST['name'],
                                        surname=request.POST['surname'],
                                        birthdate=request.POST['birthdate'],
                                        jobExperience=request.POST['jobExperience'],
                                        salary=request.POST['salary'],
                                        progLang=request.POST['progLang'],)
         response_data = f1.dic()
         request.session['has_posted_already'] = True
         return HttpResponse(json.dumps({'programmer': response_data}), content_type="application/json" )
     return HttpResponse(json.dumps({'Status' : 'error2'}) , content_type="application/json")


def prog_del_api(request, id):
    if request.method == "POST":
        prog = Programmer.objects.get(id=id)
        Programmer.objects.get(id=id).delete()
        response_data = prog.dic()
        return HttpResponse(json.dumps({'programmer': response_data , 'status':'deleted ok'}), content_type="application/json")
    return HttpResponse(json.dumps({'Status': 'error2'}), content_type="application/json")