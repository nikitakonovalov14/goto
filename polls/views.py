from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Person
# Create your views here.
global no
no=0
global yes
yes=0

def my(request):
    global no
    global yes

    key = request.POST.get("key")
    if key:
        p = Person(first_name=key)
        p.save()

    data = Person.objects.all()

    Person.objects.filter(first_name=request.GET.get("n")).delete()

    keyno = request.GET.get("no")
    keyyes = request.GET.get("yes")
    if(keyno=="забито"):
        no+=1
    if(keyyes=="сделано"):yes+=1
    key = request.POST.get("key")

#    data = [[i,item] for i, item in enumerate(data)]

    return render(request,"index.html",context={"data":data,"no":no,"yes":yes,})

