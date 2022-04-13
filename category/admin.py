from django.contrib import admin
from .models import Category  # importamos la clase del modelo


# Register your models here.

# clase, permite el llenado automatico del campo slug dependiendo del lllenado del campo 'Category Name' del formulario
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')


# registro de clases en Django manager
admin.site.register(Category, CategoryAdmin)
