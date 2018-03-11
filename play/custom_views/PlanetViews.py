from django.http import HttpResponse
from django.shortcuts import render
from ..models import Planet

def detail(request,p_id):
    planets_list = Planet.objects.order_by('-name')[0]
    context = {'name': planets_list.name}
    return render(request, 'planet/details.html', context)