from django import forms
from main.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']  # Field produk yang dapat diisi pengguna
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Menambahkan atribut HTML untuk memperbaiki tampilan form
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Masukkan nama produk'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Masukkan harga produk'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Masukkan deskripsi produk'})
