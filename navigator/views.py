from django.shortcuts import render
import datetime
# Create your views here.
def about(request):
    dr = {'students': [
        {'name': "Rakib Khan", 'age': 22, 'result': True},
        {'name': "Rahat Ali", 'age': 23, 'result': False},
        {'name': "Faysal", 'age': 24, 'result': False},
        {'name': "Fatima", 'age': 21, 'result': True},
        {'name': "Fardin", 'age': 22, 'result': True},
    ],
    }
    return render(request,'about.html',dr)

def blog(resquest):
    employees = {
        'name': "robin", 'age': 25, 'dep': 'Engineer', 'joinDate': datetime.datetime.now(),
        'list': ['Apple', 'Mango', 'Orange'],
        'fvrt': "i love Django"

    }
    return render(resquest,'blog.html', employees)