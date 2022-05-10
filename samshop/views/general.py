from django.db.models import Q
from samshop.views import Basket
from samshop.forms import SignUpForm, BasketAddProductForm
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from samshop.models import Basket, Customer, LineItem, Order, ProductDetails


# from django.db.models import Q
# from samshop.forms import SignUpForm
# from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator
# from django.contrib.auth import login, authenticate
# from samshop.models import MainCategory, SubCategory, ProductDetails


# Create your views here.


# def home(request):
#     return render(request, 'samshop/base.html')


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
    form = BasketAddProductForm()
    return render(request, 'samshop/index.html', {'page_obj': page_obj, 'form': form})


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
    form = BasketAddProductForm()

    return render(request, 'samshop/clothing.html', {'page_obj': page_obj, 'form': form})


def footwear(request):
    data = ProductDetails.objects.filter(main_category=238)

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = BasketAddProductForm()

    return render(request, 'samshop/footwear.html', {'page_obj': page_obj, 'form': form})


def jewellery(request):
    data = ProductDetails.objects.filter(main_category=239)

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = BasketAddProductForm()

    return render(request, 'samshop/jewellery.html', {'page_obj': page_obj, 'form': form})


def watches(request):
    data = ProductDetails.objects.filter(main_category=240)

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = BasketAddProductForm()

    return render(request, 'samshop/watches.html', {'page_obj': page_obj, 'form': form})


def bags(request):
    data = ProductDetails.objects.filter(main_category=236)

    paginator = Paginator(data, 51)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = BasketAddProductForm()

    return render(request, 'samshop/bags.html', {'page_obj': page_obj, 'form': form})



# def signup(request):
#     # Reference - https://github.com/scharlau/shopping_exercise_django
#
#     form = SignUpForm(request.POST)
#     if form.is_valid():
#         user = form.save()
#         user.refresh_from_db()
#         user.customer.first_name = form.cleaned_data.get('first_name')
#         user.customer.last_name = form.cleaned_data.get('last_name')
#         user.customer.address = form.cleaned_data.get('address')
#         user.save()
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect('/')
#     return render(request, 'signup.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user
    if user.is_authenticated & user.is_staff:
        return render(request, 'shop/dashboard.html')
    else:
        return redirect('/accounts/login.html')


# save order, clear basket and thank customer
def payment(request):
    basket = Basket(request)
    user = request.user
    customer = get_object_or_404(Customer, user_id=user.id)
    order = Order.objects.create(customer=customer)
    order.refresh_from_db()
    for item in basket:
        product_item = get_object_or_404(ProductDetails, id=item['product_id'])
        cart = Basket.objects.create(product=product_item, quantity=item['quantity'])
        cart.refresh_from_db()
        line_item = LineItem.objects.create(quantity=item['quantity'], product=product_item, cart=cart, order=order)

    basket.clear()
    request.session['deleted'] = 'thanks for your purchase'
    return redirect('samshop:product_list')


def purchase(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket(request)

        return render(request, 'samshop/purchase.html', {'basket': basket, 'user': user})
    else:
        return redirect('login')
