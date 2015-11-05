from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View, DetailView
from movies2.models import Movie, Rater, Rating






# Create your views here.
# def list_movies(request):
#     movies = get_list_or_404(Movie)
#     return render(request, 'movie_list.html', {'movies': movies})



# class ListMovies(ListView):
#     model = Movie
#     queryset = Movie.objects.all()
#     paginate_by = 20
#     template_name = 'movie_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_load'] = timezone.now()
#         return context






def list_all_movies(request):
    movies = get_list_or_404(Movie)
    return render(request, 'movies2/movie_list.html', {'movies': movies})


# class MovieDetail(View):
#
#     def get(self, request):
#         movie = get_object_or_404(Movie)
#
#         return render(self.request, 'movie_detail.html', {'movie': movie})


class MovieDetail(DetailView):
    model = Movie

class RaterDetail(DetailView):
    model = Rater


