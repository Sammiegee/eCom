import csv
from pathlib import Path
from django.db import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from samshop.models import MainCategory, SubCategory, ProductDetails


class Command(BaseCommand):
    def handle(self, *args, **options):

        # drop all tables to avoid duplicates
        MainCategory.objects.all().delete()
        SubCategory.objects.all().delete()
        ProductDetails.objects.all().delete()

        print("Table dropped successfully")
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
                item_name = row[1]
                retail_price = row[11]
                disc_price = row[12]
                image1 = row[13]
                image2 = row[14]
                image3 = row[15]
                image4 = row[16]
                print(count+1)
                print(row[2])

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
