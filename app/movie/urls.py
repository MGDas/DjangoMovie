from django.urls import path
from movie import views


urlpatterns = [
    path('movies/', views.MovieListView.as_view(), name='movie_list_url'),
    path('movies/<str:slug>/', views.MovieDetailView.as_view(), name='movie_detail_url')
]
