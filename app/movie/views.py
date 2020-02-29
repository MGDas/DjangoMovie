from django.views.generic import ListView
from django.views.generic import DetailView

from movie.models import Movie


class MovieListView(ListView):
    template_name = 'movie/movie_list.html'
    context_object_name = 'movies'
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/movie_detail.html'
    context_object_name = 'movie'
    slug_field = 'url'
