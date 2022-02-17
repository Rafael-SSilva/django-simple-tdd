from django.shortcuts import render
from .models import Animal


def index(request):
    context = {'characteristics': None}
    search = request.GET.get('buscar', None)

    if search is not None:
        animals = Animal.objects.filter(name__icontains=search)
        context['characteristics'] = animals

    return render(request, 'index.html', context)
