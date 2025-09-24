from django.http import HttpResponse
from django.shortcuts import render,redirect

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


def add(request):
    return render(request,'add.html')


def add_record(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    new_member = member(firstname=fname, lastname=lname)  
    new_member.save()
    return redirect('index')  


def delete(request, id):
    person = member.objects.get(id=id)
    person.delete()
    return redirect('index')

def update(request, id):
    person = member.objects.get(id=id)
    
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        person.firstname = fname
        person.lastname = lname
        person.save()
        return redirect('index')
    
    return render(request, 'update.html', {'person': person})
