from django.db import models
from brand.models import BrandModel


# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name="cars")
    image = models.ImageField(upload_to="uploads/")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class CommentModel(models.Model):
    post = models.ForeignKey(
        CarModel, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
