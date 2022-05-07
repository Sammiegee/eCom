import csv
import random
import decimal
from faker import Faker
from pathlib import Path
from datetime import datetime
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from samshop.models import MainCategory, SubCategory, ProductDetails, Basket, Order, LineItem, Customer


class Command(BaseCommand):
    def handle(self, *args, **options):

        # drop all tables to avoid duplicates

        Basket.objects.all().delete()
        LineItem.objects.all().delete()
        Order.objects.all().delete()
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        ProductDetails.objects.all().delete()
        Customer.objects.all().delete()
        User.objects.all().delete()
        print("Table dropped successfully")

        fake = Faker()

        base_dir = Path(__file__).resolve().parent.parent.parent.parent

        with open(f'{base_dir}/samshop/data/flipkart_category.csv', 'r') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                try:
                    category = row[0]
                    print(category)
                    if category == "":
                        print("Skipped this one")
                        pass
                    else:
                        main_category = MainCategory.objects.create(
                            category=category,
                        )
                        print("data parsed successfully")
                        main_category.save()
                except IntegrityError:
                    pass
        print("Done with this")

        with open(f'{base_dir}/samshop/data/flipkart_category.csv', 'r') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for row in reader:
                sub_category = row[1]

                sub_category = SubCategory.objects.create(
                    sub_category=sub_category,
                )
                print("data parsed successfully")
                sub_category.save()

        with open(f'{base_dir}/samshop/data/flipkart_com-ecommerce_file.csv', 'r') as file:
            reader = csv.reader(file, delimiter=",")
            next(reader)
            for count, row in enumerate(reader):
                try:
                    item_name = row[1]
                    retail_price = row[11]
                    disc_price = row[12]
                    image1 = row[13]
                    image2 = row[14]
                    image3 = row[15]
                    image4 = row[16]
                    print(count+1)
                    print(row[2])
                    print(row[3])

                    if retail_price == "":
                        pass
                    else:

                        product_details = ProductDetails.objects.create(
                            item_name=item_name,
                            retail_price=retail_price,
                            disc_price=disc_price,
                            main_category=MainCategory.objects.get(category=row[2]),
                            sub_category=SubCategory.objects.get(sub_category=row[3]),
                            image1=image1,
                            image2=image2,
                            image3=image3,
                            image4=image4,
                        )
                        product_details.save()
                except ValueError:
                    pass
