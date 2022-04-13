from .models import Category


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)            # retorna un diccionario con los links de categoria de productos de la navbar
