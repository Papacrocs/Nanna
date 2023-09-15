from itertools import permutations
# from main_app.models import City
from math import radians, sin, cos, sqrt, atan2

def optimize_route(cities):
    shortest_distance = float('inf')
    shortest_route = None

    for route in permutations(cities):
        distance = sum(city1.distance_to(city2) for city1, city2 in zip(route[:-1], route[1:]))
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route

    return shortest_route
