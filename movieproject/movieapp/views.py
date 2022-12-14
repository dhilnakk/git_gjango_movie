from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie = Movie.objects.all()
    return render(request, 'index.html', {'key': movie})

def details(request, movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'key':movie})

def add_movie(request):
    if request.method == 'POST':
        mname=request.POST.get('name')
        mdesc = request.POST.get('desc')
        myear = request.POST.get('year')
        mimg = request.FILES['img']
        movie=Movie(name=mname,desc=mdesc,year=myear,img=mimg)
        movie.save()
    return render(request,'add.html')
def update(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'fkey':form,'mkey':movie})
def delete(request,movie_id):
    if request.method == 'POST' :
        movie=Movie.objects.get(id=movie_id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')