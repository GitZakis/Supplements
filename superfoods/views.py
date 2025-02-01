from django.shortcuts import render,get_object_or_404,redirect
from django.template.defaulttags import comment

from .models import  Products,Categories,Manufacturers
from django.utils import timezone



# Create your views here.
def post_list(request):
    products = Products.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'products':products})


def post_detail(request, pk):
    products_detail = get_object_or_404(Products, pk=pk)
    return render(request, 'blog/post_detail.html', {'products_detail': products_detail})