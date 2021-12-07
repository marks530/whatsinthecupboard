from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    q_set = Product.objects.all()
    for product in q_set:
        print(product)
    return render(request, 'hello.html', {'name': 'Mark'})
