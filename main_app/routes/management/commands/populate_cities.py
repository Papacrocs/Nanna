from django.core.management.base import BaseCommand
from routes.models import City, State

# This class is a required class for custom django-admin commands
class Command(BaseCommand):
    help = 'Populates the database with cities'
    # This function is a required function for custom django-admin commands
    def handle(self, *args, **options):
        states = [
            {'name': 'Abia', 'lat': 5.5320, 'lon': 7.4860},
            {'name': 'Adamawa', 'lat': 9.2091, 'lon': 12.4818}, 
            {'name': 'Akwa Ibom', 'lat': 4.9434, 'lon': 7.8699},
            {'name': 'Anambra', 'lat': 6.2102, 'lon': 7.0698},
            {'name': 'Bauchi', 'lat': 10.3157, 'lon': 9.8448},
            {'name': 'Bayelsa', 'lat': 4.9267, 'lon': 6.2676},
            {'name': 'Benue', 'lat': 7.1907, 'lon': 8.1314},
            {'name': 'Borno', 'lat': 11.8333, 'lon': 13.1500},
            {'name': 'Cross River', 'lat': 5.8714, 'lon': 8.7081},
            {'name': 'Delta', 'lat': 5.7110, 'lon': 5.3200},
            {'name': 'Ebonyi', 'lat': 6.3162, 'lon': 8.1164},
            {'name': 'Edo', 'lat': 6.5440, 'lon': 5.8980},
            {'name': 'Ekiti', 'lat': 7.6704, 'lon': 5.2204},
            {'name': 'Enugu', 'lat': 6.4413, 'lon': 7.4988},
            {'name': 'Gombe', 'lat': 10.2903, 'lon': 11.1673},
            {'name': 'Imo', 'lat': 5.4842, 'lon': 7.0281},
            {'name': 'Jigawa', 'lat': 12.5709, 'lon': 8.0904},
            {'name': 'Kaduna', 'lat': 10.5167, 'lon': 7.4333},
            {'name': 'Kano', 'lat': 12.0022, 'lon': 8.5132},
            {'name': 'Katsina', 'lat': 12.9908, 'lon': 7.6018},
            {'name': 'Kebbi', 'lat': 12.4539, 'lon': 4.1975},
            {'name': 'Kogi', 'lat': 7.8000, 'lon': 6.7333},
            {'name': 'Kwara', 'lat': 8.5000, 'lon': 4.5500},
            {'name': 'Lagos', 'lat': 6.5244, 'lon': 3.3792},
            {'name': 'Nasarawa', 'lat': 8.4900, 'lon': 8.5200},
            {'name': 'Niger', 'lat': 9.5965, 'lon': 6.5560},
            {'name': 'Ogun', 'lat': 7.1500, 'lon': 3.3500},
            {'name': 'Ondo', 'lat': 7.2500, 'lon': 5.2000},
            {'name': 'Osun', 'lat': 7.9833, 'lon': 4.5667},
            {'name': 'Oyo', 'lat': 7.9707, 'lon': 3.5900},
            {'name': 'Plateau', 'lat': 9.9297, 'lon': 8.8921},
            {'name': 'Rivers', 'lat': 4.8100, 'lon': 7.0100},
            {'name': 'Sokoto', 'lat': 13.0667, 'lon': 5.2333},
            {'name': 'Taraba', 'lat': 7.8500, 'lon': 9.7833},
            {'name': 'Yobe', 'lat': 11.7500, 'lon': 11.9667},
            {'name': 'Zamfara', 'lat': 12.1700, 'lon': 6.6600},
            {'name': 'Abuja', 'lat': 9.0765, 'lon': 7.3986},

        ]
