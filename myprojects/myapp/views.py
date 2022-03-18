from django.shortcuts import render
from .models import place,team

# Create your views here.


from django.http import HttpResponse


def index(request):
    obj = place.objects.all()
    obj_2 = team.objects.all()

    return render(request,'index.html',{'result':obj,'teams':obj_2})



