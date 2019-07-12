from django.shortcuts import render
from .models import Movie


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def detail(request,link):

    return render(request,'detail.html',locals())


def search_form(request):

    if request.method == 'POST':

        movie_name = request.POST.get('movie_name')
        try:
            movie = Movie.objects.filter(movie_name=movie_name)[0]
        except Exception as e:
            pass
    return render(request,'second.html',locals())

































