from django.shortcuts import render, redirect

# Create your views here.
from recipes_app.recipes.forms import CreateRecipeForm, DeleteRecipeForm, EditRecipeForm
from recipes_app.recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "POST":
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = CreateRecipeForm()

    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'details.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('index')

    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'recipe': recipe,
        'form': form,
    }

    return render(request, 'delete.html', context)
