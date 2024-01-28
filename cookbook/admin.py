from django.contrib import admin
from .models import Product, Recipe, RecipeProduct


class RecipeProductInline(admin.TabularInline):
    model = RecipeProduct
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    
    pass
    # list_display = ('name', 'cooked_times')  # Отображать эти поля в списке продуктов
    # search_fields = ('name')  # Позволяет искать продукты по имени
    # list_filter = ('cooked_times')  # Добавляет фильтры для количества приготовленных блюд


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeProductInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)


