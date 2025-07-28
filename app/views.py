from django.shortcuts import render, redirect,get_object_or_404
from django.urls import path
from .models import Cars, Avtosalon, Brand
from .forms import CarForm,AvtosalonForm,BrandForm

# Create your views here.

def home(request):
    avtosalon = Avtosalon.objects.all()
    cars = Cars.objects.all()
    brand = Brand.objects.all()
    context = {
        'avtosalon':avtosalon,

    }
    return render(request,'index.html',context=context)

def add_cars(request):
    if request.method == "POST":
        form = CarForm(request.POST)
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
            Avtosalon.objects.create(**form.cleaned_data)
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



# def avtosalon_brands(request):
#     brand = Brand.objects.all()
#     cars = Cars.objects.all()

#     context = {
#         'brand':brand,
#         'cars':cars,
#     }
#     return render(request,'avtosalon.html',context=context)
