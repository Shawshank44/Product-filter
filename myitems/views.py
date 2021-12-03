from django.shortcuts import render
from .models import *

# Create your views here.

def Home(request):
    brands = BrandCategory.objects.all()
    context ={
        'brands' : brands

    }
    return render(request,'home.html',context)


def items(request,slug):
    i = BrandCategory.objects.get(slug=slug)
    p = Products.objects.filter(slug=slug)
    if i == p :
        Products.objects.all()

    context ={
        'item' : i,
        'product':p
    }
    return render(request,'products.html',context)
