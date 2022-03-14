from django.http import HttpResponse
from .models import Movie
from django.shortcuts import render,redirect
from . forms import MovieForm
# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list':movie
    }
    return render(request,'index.html',context)
def details(request,movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        year = request.POST.get('year')
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        movie = Movie(name=name,description=description,year=year,image1=image1,image2=image2,image3=image3)
        movie.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    movie = Movie.objects.get(id=id)

    form = MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
