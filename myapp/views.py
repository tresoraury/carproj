from django.shortcuts import render
from rest_framework import viewsets
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars':cars})

