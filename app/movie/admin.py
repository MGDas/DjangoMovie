from django.contrib import admin

from movie.models import Category
from movie.models import Actor
from movie.models import Genre
from movie.models import Movie
from movie.models import MovieShot
from movie.models import Rating
from movie.models import RatingStar
from movie.models import Review


admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShot)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Review)
