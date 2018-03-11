from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
        planets_list = Planet.objects.order_by('-name')
        context = {'planets_list': planets_list}
        return render(request, 'star_system/index.html', context)

def detail(request, planet_id):
    return HttpResponse("You're looking at planet %s." % planet_id)