from django.urls import path
from .views import (
    home,add_avtosalon,add_brand,add_cars,
    avtosalon_pk,avtosalon_brands,car_detail,download_pdf
)

urlpatterns = [
    path('',home,name='home'),
    path('add_cars/',add_cars,name='add_cars'),
    path('add_brand/',add_brand,name='add_brand'),
    path('add_avtosalon/',add_avtosalon,name='add_avtosalon'), #-----

    path('avtosalon_pk/<int:pk>/',avtosalon_pk,name='avtosalon_pk'), # avtosalonga kirish pk
    path('avtosalon_brands/<int:pk>/<int:car_pk>/',avtosalon_brands,name='avtosalon_brands'), #sortirovka pk

    path('car_detail/<int:pk>',car_detail,name="car_detail"),
    path('download_pdf/<int:pk>',download_pdf,name="download_pdf"),
]

# avtosalon/<int:pk>/brand/<int:car_pk>
# 'avtosalon/(?P<pk>[0-9]+)/brand/(?P<car_pk>[0-9]+)\\Z'