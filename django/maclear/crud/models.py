from django.db import models

# Create your models here.

class Status(models.IntegerChoices):
	Active	 = 1
	Unactive = 0

class Store(models.Model):
	"""docstring for Store"""
	name 		= models.CharField(max_length = 255)
	desc		= models.TextField(blank = True)
	status 		= models.IntegerField(choices = Status.choices, default = Status.Active)
	created 	= models.DateTimeField(auto_now_add = True)
	updated 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return f"{self.name}, {self.created}"

class Product(models.Model):
	"""docstring for Product"""
	store 		= models.ForeignKey(Store, on_delete = models.CASCADE)
	name 		= models.CharField(max_length = 255)
	price 		= models.IntegerField(default = 0)
	desc		= models.TextField(blank = True)
	qty			= models.IntegerField(default = 0)
	status 		= models.IntegerField(choices = Status.choices, default = Status.Active)
	created 	= models.DateTimeField(auto_now_add = True)
	updated 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return f"{self.name}, {self.price}, {self.created}"

class Customer(models.Model):
	"""docstring for Customer"""
	name 		= models.CharField(max_length = 255)
	address		= models.TextField(blank = True)
	status 		= models.IntegerField(choices = Status.choices, default = Status.Active)
	created 	= models.DateTimeField(auto_now_add = True)
	updated 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name
		

class Transaction(models.Model):
	"""docstring for Transaction"""
	customer 	= models.ForeignKey(Customer, on_delete = models.CASCADE)
	product 	= models.ForeignKey(Product, on_delete = models.CASCADE)
	qty			= models.IntegerField(default = 0)
	total		= models.IntegerField(default = 0)
	status 		= models.IntegerField(choices = Status.choices, default = Status.Active)
	created 	= models.DateTimeField(auto_now_add = True)
	updated 	= models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.customer.name

class ProductImage(models.Model):
	"""docstring for ProductImage"""
	file = models.ImageField(upload_to = 'static/')
	description = models.TextField(blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def delete(self,*args,**kwargs):
		import os
		if os.path.isfile(self.file.path):
			os.remove(self.file.path)
		super(ProductImage, self).delete(*args,**kwargs)
		