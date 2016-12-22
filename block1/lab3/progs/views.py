from django.shortcuts import render_to_response ,redirect , render
import json

progs_list = []

def getJson(request):
    file = open("programmers.json", "r")
    programmers = json.load(file)
    return programmers

def home (request):
    return render(request, 'index.html')

def progs_all(request):
    programmers = getJson("programmers.json")
    return render( request , "show.html" , {'programmers': programmers})

def progs_by_id(request, id):
    progs = getJson("programmers.json")
    prog = {}
    for i in progs:
        if i['id'] == int(id):
            prog = i
            break
    return render(request , "prog.html" , {'prog': prog})
