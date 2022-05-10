from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class MainCategory(models.Model):
    category = models.CharField(unique=True, max_length=200)


class SubCategory(models.Model):
    sub_category = models.CharField(unique=True, max_length=200)


class ProductDetails(models.Model):
    item_name = models.CharField(max_length=2000)
    # brand = models.CharField(max_length=200)
    main_category = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    retail_price = models.IntegerField()
    disc_price = models.IntegerField()
    image1 = models.URLField(max_length=1000)
    image2 = models.URLField(max_length=1000)
    image3 = models.URLField(max_length=1000)
    image4 = models.URLField(max_length=1000)

    def __str__(self):
        return f'{self.item_name},{self.disc_price}'


class Basket(models.Model):
    product = models.ForeignKey('samshop.ProductDetails', on_delete=models.CASCADE, related_name='baskets')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product},{self.quantity},{self.created_date}'


class Customer(models.Model):
    # Reference https://github.com/scharlau/shopping_exercise_django
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}, {self.customer.address}'

    class Meta:
        db_table = 'customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()


class LineItem(models.Model):
    # Reference https://github.com/scharlau/shopping_exercise_django
    quantity = models.IntegerField()
    product = models.ForeignKey('samshop.ProductDetails', on_delete=models.CASCADE)
    basket = models.ForeignKey('samshop.Basket', on_delete=models.CASCADE)
    order = models.ForeignKey('samshop.Order', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity},{self.product},{self.basket},{self.order},{self.created_date}'


class Order(models.Model):
    # Reference https://github.com/scharlau/shopping_exercise_django
    customer = models.ForeignKey('samshop.Customer', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer},{self.created_date}'
