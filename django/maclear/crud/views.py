from django.shortcuts import render, redirect
from django.http import HttpResponse
from crud.models import Product
from crud.forms import EditProductForm, AddProductForm

# Create your views here.
def products(request):
	products = Product.objects.all()
	context = {
		'title': 'CRUD - All Products',
		'products': products
	}
	return render(request, 'crud/allproduct.html', context)

def product_read(request, id = 0):
	if type == 0:
		return redirect('/')
	product = Product.objects.get(pk = id)
	context = {
		'title': 'CRUD - Read %s' % product.name,
		'product': product
	}
	return render(request, 'crud/readproduct.html', context)

def product_edit(request, id = 0):
	if type == 0:
		return redirect('/')
	product = Product.objects.get(pk = id)
	editForm = EditProductForm(instance = product)
	if request.method == 'POST':
		editForm = EditProductForm(request.POST, instance = product)
		if editForm.is_valid():
			editForm.save()
			return redirect('/crud/products')
		else:
			return HttpResponse('NOT Valid please try again <a href="/">')
	context = {
		'title': 'CRUD - Update %s' % product.name,
		'product': product,
		'form': editForm
	}
	return render(request, 'crud/editproduct.html', context)

def product_delete(request, id = 0):
	if type == 0:
		return redirect('/')
	product = Product.objects.get(pk = id)
	if product:
		Product.objects.get(pk = id).delete()
	return redirect('/crud/products')

def product_add(request):
	addForm = AddProductForm(request.POST)
	if request.method == 'POST':
		if addForm.is_valid():
			addForm.save()
			return redirect('/crud/products')
		else:
			return HttpResponse('NOT Valid please try again <a href="/">')
	context = {
		'title': 'CRUD - Add Product',
		'form': addForm
	}
	return render(request, 'crud/addproduct.html', context)
