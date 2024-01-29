from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, RecipeProduct, Product


def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    product = get_object_or_404(Product, pk=product_id)
    
    
    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight = weight
    recipe_product.save()
    
    
    return HttpResponse(f"Product added/updated to recipe: {recipe.name}")

def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    for recipe_product in recipe.products_set.all():
        recipe_product.product.times_cooked += 1
        recipe_product.product.save()

    return HttpResponse(f"Recipe cooked: {recipe.name}")


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product) \
                                                .filter(recipeproduct__weight__lt=10)
        
        
    return render(request, 'cookbook/index.html', {'recipe': recipes_without_product})
