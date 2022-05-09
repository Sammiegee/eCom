from django.db.models import Q
from samshop.forms import SignUpForm
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from samshop.models import MainCategory, SubCategory, ProductDetails


# Create your views here.


def home(request):
    return render(request, 'samshop/base.html')



def signup(request):
    # Reference https://github.com/scharlau/shopping_exercise_django/blob/main/shop/views/general.py

    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.customer.address = form.cleaned_data.get('address')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password= password)
        login(request, user)
        return redirect('/')
    return render(request, 'samshop/signup.html', {'form': form})



def index(request):
    data = ProductDetails.objects.all()

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'samshop/index.html', {'page_obj': page_obj})


def search(request):

    if request.method == "POST":
        query = request.POST.get('query')
        if query:
            data = ProductDetails.objects.filter(
                Q(item_name__icontains=query) | Q(main_category__category__icontains=query)
                | Q(sub_category__sub_category__icontains=query)
            )
            paginator = Paginator(data, 51)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'samshop/search.html', {'page_obj': page_obj})

    return redirect('samshop:index')



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




