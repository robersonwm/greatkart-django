from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category


# Create your views here.

# asocia la vista de store al template correspondiente para la visualización en el navegador
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)  # recupera los productos disponibles=True
        product_count = products.count()  # numero de productos en la BD
    context = {
        'products': products,
        'product_count': product_count,
    }

    # context: conjunto de tags para visualizar informacion en el template
    return render(request, 'store/store.html', context)


# vista, asocia el templete para mostrar el detalle del producto
def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)
