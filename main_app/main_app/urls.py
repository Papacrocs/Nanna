from django.urls import path
from routes import views

# Add the 'routes' app here
urlpatterns = [
    path('', views.home, name='home'),
    path('routes/optimize/', views.optimize_route_view, name='optimize_route'),
]
