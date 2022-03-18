from django.http import HttpResponse
from .models import Movie
from django.shortcuts import render,redirect
from . forms import MovieForm
from django.db.models import Q
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

    form = MovieForm(request.POST or None,instance=movie)
    if form.is_valid ():
        form.save()
        return redirect('movieapp:index')
    return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
def SearchResult(request):
    movie = None
    query = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        movie = Movie.objects.all().filter(Q(name=query) | Q(description=query))

    return render(request,'search.html',{'query':query,'movie':movie})

