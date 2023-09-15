from django.shortcuts import render
from django.http import JsonResponse
from .models import City, Route
from .utils import optimize_route

def home(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'home.html', context)

    # return render(request, 'home.html')
    # return render(request, 'home.html', {'cities': cities})
    
def optimize_route_view(request):
    city_ids = request.GET.getlist('city_ids[]')
    cities = City.objects.filter(id__in=city_ids)
    route = optimize_route(cities)
    data = [{'name': city.name, 'latitude': city.latitude, 'longitude': city.longitude} for city in route]
    return JsonResponse(data, safe=False)
