from django.contrib import admin
from .models import Products, Categories, Manufacturers

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Manufacturers)

# Register your models here.
