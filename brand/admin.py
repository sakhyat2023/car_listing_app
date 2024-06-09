from django.contrib import admin
from .models import BrandModel

# Register your models here.

class AdminBrandModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    list_display = ["name", "slug"]

admin.site.register(BrandModel, AdminBrandModel)