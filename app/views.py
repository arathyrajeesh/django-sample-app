from django.http import HttpResponse
from django.shortcuts import render

from app.models import member


def main(request):
    return render(request,'main.html')

def index(request):
    person=  member.objects.all().values()
    return render(request,'index.html',{'person':person})

def details(request, id):
    persons = member.objects.get(id=id)
    return render(request,'details.html',{'persons':persons})


def testing(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return render(request,'testing.html',context)
