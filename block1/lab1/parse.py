import json


class Programmer(object):
    def __init__(self, id = None, name = None, surname = None,  birthdate = None, jobExperience = None, salary = None, progLang = None):
        self.id = id
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.jobExperience = jobExperience
        self.salary = salary
        self.progLang = progLang

    def parseFromDict(self, dict):
        self.__init__(dict.get("id"), dict.get("name"), dict.get("surname"), dict.get("birthdate"), dict.get("jobExperience"), dict.get("salary"), dict.get("progLang"))
        return self

    def toString (self):
        _str = ""
        _str += str(self.id) + '\n'
        _str += self.name + '\n'
        _str += self.surname + '\n'
        _str += self.birthdate + '\n'
        _str += str(self.jobExperience) + '\n'
        _str += str(self.salary) + '\n'
        _str += self.progLang + '\n'*2
        return _str

    def toDict(self):
        return {'id': self.id,
				'name' : self.name, 
				'surname' : self.surname, 
				'birthdate' : self.birthdate, 
				'jobExperience' : self.jobExperience,
				'salary' : self.salary,
				'progLang': self.progLang }


def parseFile(filename):
    file = open(filename, "r")
    programmers = json.load(file);
    # print (programmers)
    prog_list = []

    for i in programmers:
       prog_list.append(Programmer().parseFromDict(i))
    file.close()
    return prog_list

def parseRequest(request):
    dictionary = {}
    if request.find('=') == -1:
        return None
    for s in request.split('&'):
        arglist = s.split('=', 1)
        dictionary.update({arglist[0] : arglist[1]})
    return dictionary

def getJson(request):
    if request == "all":
        file = open("programmers.json", "r")
        programmers = json.load(file);
        return json.dumps(programmers, sort_keys=True, indent=4)
    elif request == "amount":
        prog_list = parseFile("programmers.json")
        return len(prog_list)
    argdict = parseRequest(request)

    if argdict == None:
        return '[{"exception" : "wrong args"}]'
    prog_list = parseFile("programmers.json")
    new_prog_list = prog_list.copy()
    for prog in prog_list:
        for key, value in argdict.items():
            if key == "progLang":
                if prog.progLang != value:
                    new_prog_list.remove(prog)
                    break
            elif key == "jobExplessthan":
                if prog.jobExperience > float(value):
                    new_prog_list.remove(prog)
                    break
            elif key == "salarylessthan":
                if prog.salary > int(value):
                     new_prog_list.remove(prog)
                     break
            elif key == "jobExpgreatthan":
                if prog.jobExperience < float(value):
                    new_prog_list.remove(prog)
                    break
            elif key == "salarygreatthan":
                if prog.salary < int(value):
                    new_prog_list.remove(prog)
                    break
            else:
                return '[{"exception" : "wrong args"}]'
    returnList = []
	
    for prog in new_prog_list:
        returnList.append(prog.toDict())
    return json.dumps(returnList, sort_keys=True, indent=4)
