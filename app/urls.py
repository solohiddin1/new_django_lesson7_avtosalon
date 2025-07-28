from django.urls import path
from .views import home,add_avtosalon,add_brand,add_cars,avtosalon_pk,avtosalon_brands

urlpatterns = [
    path('',home,name='home'),
    path('add_cars/',add_cars,name='add_cars'),
    path('add_brand/',add_brand,name='add_brand'),
    path('add_avtosalon/',add_avtosalon,name='add_avtosalon'), #-----

    path('avtosalon_pk/<int:pk>/',avtosalon_pk,name='avtosalon_pk'), # avtosalonga kirish pk
    path('avtosalon_brands/<int:pk>/<int:car_pk>/',avtosalon_brands,name='avtosalon_brands'), #sortirovka pk
]
# avtosalon/<int:pk>/brand/<int:car_pk>
# 'avtosalon/(?P<pk>[0-9]+)/brand/(?P<car_pk>[0-9]+)\\Z'