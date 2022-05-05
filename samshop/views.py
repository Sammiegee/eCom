from django.shortcuts import render
from .models import ProductDetails

# Create your views here.


def home(request):
    return render(request, 'samshop/base.html')


def index(request):
    # if request.method == "POST":
    #     station = request.POST.get('station_name')
    #     request.session['station_name'] = station

    data = ProductDetails.objects.filter(catogory="Clothing")

    return render(request, 'samshop/index.html', {'data':data})


def login(request):
    return render(request, 'samshop/login.html')

