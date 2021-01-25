from django.contrib import admin

# Register your models here.
from .models import Product, Store, Customer, Transaction, ProductImage

models = (Product, Store, Customer, Transaction, ProductImage)
for model in models:
	admin.site.register(model)