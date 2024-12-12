from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, car_list

router = DefaultRouter()
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', car_list, name='car_list'),
]