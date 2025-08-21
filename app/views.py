from django.shortcuts import render, redirect,get_object_or_404
from django.urls import path
from .models import Cars, Avtosalon, Brand
from .forms import CarForm,AvtosalonForm,BrandForm
from django.db.models import Q
from django.http import HttpResponse
# from django.response import response
from PIL import Image

import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from django.conf import settings
import os

# Create your views here.

def home(request):
    query = request.GET.get('q')

    avtosalon = Avtosalon.objects.all()
    cars = Cars.objects.all()
    brand = Brand.objects.all()
    
    
    if query:
        avtosalon = avtosalon.filter(
            Q(title__icontains=query) |
            Q(context__icontains=query)
        )

    context = {
        'avtosalon':avtosalon,
        'query': query,

    }
    return render(request,'index.html',context=context)

def add_cars(request):
    if request.method == "POST":
        form = CarForm(request.POST,request.FILES)
        if form.is_valid():
            Cars.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = CarForm()
    
    return render(request,'add_cars.html',{'form':form})

def add_avtosalon(request):
    if request.method == "POST":
        form = AvtosalonForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # Avtosalon.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = AvtosalonForm()
    
    return render(request,'add_avtosalon.html',{'form':form})

def add_brand(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BrandForm()
    
    return render(request,'add_brand.html',{'form':form})


def avtosalon_pk(request,pk):
    avtosalon = get_object_or_404(Avtosalon,pk = pk)
    brands = Brand.objects.filter(brand_salon = avtosalon)
    print('=======11111111111111>',brands)
    print('=======11111111111111>',avtosalon)
    # cars = Cars.objects.all()

    context = {
        # 'cars':cars,
        'brands':brands,
        'avtosalon':avtosalon,
    }
    return render(request,'avtosalon.html',context=context)

def avtosalon_brands(request,pk,car_pk):
    avtosalon = get_object_or_404(Avtosalon,pk=pk)
    print('------------->>>>>>>>>>',avtosalon,pk)
    brands = Brand.objects.filter(brand_salon = avtosalon)
    print('------------->>>>>>>>>>',brands,car_pk)
    cars = Cars.objects.filter(salon_id = pk,brand_id = car_pk)
    print('------------->>>>>>>>>>',cars)
    
    context = {
        'brands':brands,
        'cars':cars,
        'avtosalon':avtosalon   
    }
    return render(request,'avtosalon.html',context=context) 

def car_detail(request,pk):
    car = get_object_or_404(Cars,pk=pk)

    context = {
        "car":car
    }
    return render(request,"car_detail.html",context=context)

def gemerate_pdf(car_detail,qr_code_image):
    # try:
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment:filename="car_details.pdf"'

    c = canvas.Canvas(response ,pagesize=letter)
    width , height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100,height-50, "Car details")

    c.setFont("Helvetica",12)
    y = height - 100
    
    for k , v in car_detail.items():
        if k != "image":
            c.drawString(100,y,f"{k} : {v}")
            y -= 20

    c.drawImage(qr_code_image,width - 120, height - 120, width=100, height=100)
    # c.drawImage(qr_code_image,100, y-100,width=100, height=100)

    if car_detail["image"]:
        y -= 400
        c.drawImage(car_detail["image"],100, y , height=300, width=300)

    c.save()
    print(F"Pdf generated successfully! : Filename:{response}")
    return response
    # except Exception as e:
    #     raise HttpResponseBadRequest(f"Error : {e}!")

def download_pdf(request,pk):
    car = get_object_or_404(Cars,pk=pk)

    car_details = {
        "salon":car.salon,
        "brand":car.brand,
        "model":car.model,
        "price":car.price,
        "year":car.year,
        "color":car.color,
        "image":car.image.path,
        "created_at":car.created_at,
        "updated_at":car.updated_at,
    }
    # qr_data = f"google.com"
    qr_data = f"{car.model},{car.brand}: Price:{car.price}"
    img = qrcode.make(qr_data)
    
    img_path = os.path.join(settings.MEDIA_ROOT,'qr_images', f"car_{pk}.png")
    # img_path = f"car_{pk}.png"
    img.save(img_path)

    # context = {
    #     "car":car
    # }
    return gemerate_pdf(car_detail=car_details,qr_code_image=img_path)


# def avtosalon_brands(request):
#     brand = Brand.objects.all()
#     cars = Cars.objects.all()

#     context = {
#         'brand':brand,
#         'cars':cars,
#     }
#     return render(request,'avtosalon.html',context=context)
