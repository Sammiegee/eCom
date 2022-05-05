from django.db import models

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
