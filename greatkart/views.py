# from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product  # importa el modelo de Productos desde la app 'store'


def home(request):
    # return HttpResponse('Homepage')
    # recupera los productos disponibles=True
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products,
    }
    # llama al template que se visualizará en el navegador
    return render(request, 'home.html', context)
