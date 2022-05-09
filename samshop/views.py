from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from samshop.models import MainCategory, SubCategory, ProductDetails


# Create your views here.


def home(request):
    return render(request, 'samshop/base.html')


def login(request):
    return render(request, 'registration/login.html')


def index(request):
    data = ProductDetails.objects.all()

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'samshop/index.html', {'page_obj': page_obj})


def search(request):
    if request.method == "POST":
        query = request.POST.get('query')
        data = ProductDetails.objects.filter(
            Q(item_name__icontains=query) | Q(main_category__category__icontains=query)
            | Q(sub_category__sub_category__icontains=query)
        )
        paginator = Paginator(data, 51)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    return render(request, 'samshop/search.html', {'page_obj': page_obj})


def clothing(request):
    data = ProductDetails.objects.filter(main_category=237)

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'samshop/clothing.html', {'page_obj': page_obj})


def footwear(request):
    data = ProductDetails.objects.filter(main_category=238)

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'samshop/footwear.html', {'page_obj': page_obj})


def jewellery(request):
    return render(request, 'samshop/jewellery.html')


def watches(request):
    return render(request, 'samshop/watches.html')


def bags(request):
    return render(request, 'samshop/bags.html')




