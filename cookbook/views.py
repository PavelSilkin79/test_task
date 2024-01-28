from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Recipe, RecipeProduct, Product
from django.db.models import Sum


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe = Recipe.objects.get(id=recipe_id)
    product = Product.objects.get(id=product_id)

    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight = weight
    recipe_product.save()

    return JsonResponse({'success': True})

def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')

    recipe = Recipe.objects.get(id=recipe_id)
    for product in recipe.products.all():
        product.cooked_times += 1
        product.save()

    return JsonResponse({'success': True})


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')

    recipes = Recipe.objects.annotate(total_weight=Sum('recipeproduct__weight')) \
                            .filter(recipeproduct__product_id=product_id, total_weight__lt=20)

    context = {'recipes': recipes}

    return render(request, 'cookbook/index.html', context)
