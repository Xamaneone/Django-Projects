from django.db import models


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(
        max_length=30,
    )
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=250,
    )
    time = models.IntegerField()

    def ingredients_as_list(self):
        return self.ingredients.split(", ")
