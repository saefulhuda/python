from django import forms
from crud.models import Product, Store

STYLE = 'form-control'
class EditProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'desc', 'price', 'qty')
		widgets = {
		'name': forms.TextInput(attrs = {
			'class': STYLE, 
			'placeholder': 'Nama Lengkap',
			'tabindex': 1,
			'autofocus': ''
			}),
		'desc': forms.Textarea(attrs = {
			'class': STYLE,
			}),
		'price': forms.NumberInput(attrs = {
			'class': STYLE,
			'placeholder': 'Rp. ',
			'tabindex': 3,
			'required': ''
			}),
		'qty': forms.NumberInput(attrs = {
			'class': STYLE,
			'tabindex': 3,
			'required': ''
			}),
		}

class AddProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ('name', 'desc', 'price', 'qty', 'store')
		widgets = {
		'name': forms.TextInput(attrs = {
			'class': STYLE, 
			'placeholder': 'Nama Lengkap',
			'tabindex': 1,
			'autofocus': ''
			}),
		'desc': forms.Textarea(attrs = {
			'class': STYLE,
			}),
		'price': forms.NumberInput(attrs = {
			'class': STYLE,
			'placeholder': 'Rp. ',
			'tabindex': 3,
			'required': ''
			}),
		'qty': forms.NumberInput(attrs = {
			'class': STYLE,
			'tabindex': 3,
			'required': ''
			}),
		'store': forms.Select(
			attrs = {'class': 'form-control selectric'}
			)
		}