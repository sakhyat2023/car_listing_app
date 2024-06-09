from django.contrib import admin
from .models import CarModel, CommentModel

# Register your models here.

class AdminCarModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["name", "slug"]
    
admin.site.register(CarModel, AdminCarModel)

admin.site.register(CommentModel)