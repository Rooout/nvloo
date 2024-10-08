from django import forms
from main.models import Product
from django.utils.html import strip_tags

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

    # Membersihkan dan validasi nama produk
    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()
        if not name:
            raise forms.ValidationError("Nama produk tidak boleh kosong.")
        return strip_tags(name)

    # Membersihkan dan validasi harga produk
    def clean_price(self):
        price = self.cleaned_data.get("price")
        if not price or price <= 0:
            raise forms.ValidationError("Harga produk harus lebih dari 0.")
        return price
    
    # Membersihkan dan validasi deskripsi produk
    def clean_description(self):
        description = self.cleaned_data.get("description", "").strip()
        if not description:
            raise forms.ValidationError("Deskripsi produk tidak boleh kosong.")
        return strip_tags(description)
