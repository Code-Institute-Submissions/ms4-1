from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """The view to show all the products, including"""

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """The view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'products': products,
    }

    return render(request, 'products/product_detail.html', context)