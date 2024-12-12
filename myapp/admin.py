from django.contrib import admin
from .models import Car

@admin.register(Car)
class Caradmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price')
    search_fields = ('make', 'model')
