from django.http import HttpResponse
from django.shortcuts import render
from ..models import Planet

def overview(request,ss_id):
    planets_list = Planet.objects.order_by('-name')
    print(planets_list)
    context = {'planets_list': planets_list}
    return render(request, 'star_system/index.html', context)