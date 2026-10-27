from django.contrib import admin
from .models import Product, Shop

admin.site.register((Shop, Product))
