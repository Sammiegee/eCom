from django.test import Client, TestCase
from django.urls import reverse
from .models import ProductDetails


# Create your tests here.
class SamshopIndexTests(TestCase):

    def test_index_text(self):
        client = Client()
        response = client.get('/index')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clothing")
        self.assertContains(response, "Footwear")
        self.assertContains(response, "Jewellery")
        self.assertContains(response, "Watches")
        self.assertContains(response, "Bags, Wallets & Belts")
        self.assertContains(response, "Samshop Retails")
        self.assertTemplateUsed(response, 'samshop/index.html')


class SamshopCategoryTests(TestCase):

    def footwear_category_text(self):
        client = Client()
        response = client.get('/footwear')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Give your feet a special treat and step out with confidence")
        self.assertTemplateUsed(response, 'samshop/footwear.html')

    def jewellery_category_text(self):
        client = Client()
        response = client.get('/jewellery')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Check out our finely selected pieces of jewellery")
        self.assertTemplateUsed(response, 'samshop/jewellery.html')

    def clothing_category_text(self):
        client = Client()
        response = client.get('/clothing')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Browse our selection of clothing items")
        self.assertTemplateUsed(response, 'samshop/clothing.html')

    def watches_category_text(self):
        client = Client()
        response = client.get('/watches')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Browse our selection of clothing items")
        self.assertTemplateUsed(response, 'samshop/watches.html')

    def bags_category_text(self):
        client = Client()
        response = client.get('/watches')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The finest Bags, Wallets and Belts collections around")
        self.assertTemplateUsed(response, 'samshop/bags.html')


# class SearchTests(TestCase):
#
#     def search_test(self):
#         client = Client()
#         response = client.get('/index')
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "About Air Pollution")
#         self.assertContains(response, "Related links")
#         self.assertTemplateUsed(response, 'samshop/index.html')

