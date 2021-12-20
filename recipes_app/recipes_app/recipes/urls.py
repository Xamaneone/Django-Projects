from django.urls import path

from recipes_app.recipes.views import index, create_recipe, edit_recipe, delete_recipe, recipe_details

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('details/<int:pk>', recipe_details, name='recipe details'),
    path('edit/<int:pk>', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
]
