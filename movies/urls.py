from django.urls import path
from . import views


urlpatterns = [
    path('', views.movies, name='movies'),
    path('<slug:slug>/', views.movie, name='movie'),
]
