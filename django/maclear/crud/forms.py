from django import forms
from crud.models import Product, Store, ProductImage
from PIL import Image
from django.core.files import File

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

class ProductImageForm(forms.ModelForm):
	x = forms.FloatField(widget=forms.HiddenInput())
	y = forms.FloatField(widget=forms.HiddenInput())
	width = forms.FloatField(widget=forms.HiddenInput())
	height = forms.FloatField(widget=forms.HiddenInput())

	class Meta:
		model = ProductImage
		fields = ('file', 'x', 'y', 'width', 'height', 'description')
		widgets = {
		'file': forms.FileInput(attrs = {'class': STYLE}),
		'description': forms.Textarea(attrs = {'class': STYLE})
		}

	def save(self):
		photo = super(ProductImageForm, self).save()

		x = self.cleaned_data.get('x')
		y = self.cleaned_data.get('y')
		w = self.cleaned_data.get('width')
		h = self.cleaned_data.get('height')

		image = Image.open(photo.file)
		cropped_image = image.crop((x, y, w+x, h+y))
		resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
		resized_image.save(photo.file.path)

		return photo