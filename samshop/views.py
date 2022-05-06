from django.shortcuts import render
from django.core.paginator import Paginator
from samshop.models import MainCategory, SubCategory, ProductDetails

# Create your views here.


def home(request):
    return render(request, 'samshop/base.html')


def index(request):
    # if request.method == "POST":
    #     station = request.POST.get('station_name')
    #     request.session['station_name'] = station

    data = ProductDetails.objects.filter(main_category=237)

    paginator = Paginator(data, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # return render(request, 'samshop/index.html')
    return render(request, 'samshop/index.html', {'page_obj': page_obj})


def login(request):
    return render(request, 'registration/login.html')

