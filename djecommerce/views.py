from django.shortcuts import render


def checkout(request):
    return render(request, 'checkout-page.html')


def products(request):
    return render(request, 'product-page.html')
