from django.shortcuts import render
from .models import Movie
from django.db.models import Q


def movies(request):
    context = {}

    if request.method == "GET":
        query = request.GET.get('search') or None

        if query:
            context = {
                'movies': Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
            }
        else:
            context = { 'movies': Movie.objects.all() }

    return render(request=request, template_name='index.html', context=context)


def movie(request, slug):
    obj = Movie.objects.get(slug=slug)
    obj.views += 1

    context = { 'movie': obj }
    obj.save()

    return render(request=request, template_name='detail.html', context=context)

