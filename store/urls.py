
from django.urls import path
from . import views


urlpatterns = [
    # asocia la url a la vista correspondiente en views.py
    path('', views.store, name='store'),

    # asocia una path por cada producto para visualizarlos por categoria
    path('<slug:category_slug>/', views.store, name='products_by_category'),

    #asocia la path para visualizar el detalle del producto
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]