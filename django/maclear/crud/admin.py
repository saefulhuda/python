from django.contrib import admin

# Register your models here.
from .models import Product, Store, Customer, Transaction

models = (Product, Store, Customer, Transaction)
for model in models:
	admin.site.register(model)