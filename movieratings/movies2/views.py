from django.db.models import Count
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template import response
from movies2.models import Movie, Rater, Rating
from django.db.models import Avg



# Create your views here.
def list_movies(request):
    movies = get_list_or_404(Movie)
    return render(request, 'movie_list.html', {'movies': movies})
