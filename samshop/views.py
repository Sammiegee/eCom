from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'samshop/base.html')


def index(request):
    return render(request, 'samshop/index.html')