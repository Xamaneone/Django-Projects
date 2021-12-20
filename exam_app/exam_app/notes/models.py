from django.db import models


# Create your models here.

class Note(models.Model):
    title = models.CharField(
        max_length=30
    )
    content = models.TextField()
    image_url = models.URLField(
        name="Link to Image"
    )
