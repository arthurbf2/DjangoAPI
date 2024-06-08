from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.contrib import messages
from .forms import WatchedMovieForm
from .models import WatchedMovie, Movie
from django.http import JsonResponse
from django.db.models import Count
from .serializers import MostWatchedMovieSerializer


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_watched_movie(request):
    if request.method == 'POST':
        form = WatchedMovieForm(request.POST)
        if form.is_valid():
            watched_movie = form.save(commit=False)
            watched_movie.user = request.user
            watched_movie.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('watched_movies')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = WatchedMovieForm()
    return render(request, 'add_watched_movie.html', {'form': form})

@login_required
def watched_movies(request):
    movies = WatchedMovie.objects.filter(user=request.user)
    return render(request, 'watched_movies.html', {'movies': movies})

@api_view(['GET'])
def most_watched_movies(request):
    most_watched = WatchedMovie.objects.values('movie__title').annotate(watch_count=Count('movie__title')).order_by('-watch_count')[:10]
    most_watched_data = [{'title': entry['movie__title'], 'watch_count': entry['watch_count']} for entry in most_watched]
    serializer = MostWatchedMovieSerializer(most_watched_data, many=True)
    return JsonResponse(most_watched_data, safe=False)
