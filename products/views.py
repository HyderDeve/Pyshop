from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.



def index(request): # view function for viewing a page in django
    products = Product.objects.all() #for returning all products from db
    return render(request, 'index.html', 
                  {"products":products})


def product_listing(request):
    return render(request, 'product_listing.html')
