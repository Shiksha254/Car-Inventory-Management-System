from django.shortcuts import render, redirect, get_object_or_404
from .models import Car
from .forms import CarForm
from django.template import loader

# Create your views here.
def home(request):
    cars = Car.objects.all()[:5]  # Fetch all cars from the database
    return render(request, 'CRUD/home.html', {'cars': cars})

def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_list')  # Redirect to the car list view
    else:
        form = CarForm()  # Define the form for GET requests

    return render(request, 'CRUD/create_car.html', {'form': form})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'CRUD/detail.html', {'car': car})


def car_list(request):
    cars = Car.objects.all()  # Fetch all cars from the database
    return render(request, 'CRUD/home.html', {'cars': cars})

def update_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)

    return render(request, 'CRUD/update_car.html', {'form': form, 'car': car})

def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')  # Redirect to the car list view
    return render(request, 'CRUD/delete_car_confirm.html', {'car': car})