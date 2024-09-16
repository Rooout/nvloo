from django.db import models
import uuid  # untuk membuat UUID sebagai primary key

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    email = models.EmailField(max_length=255)  # Tambahkan field untuk email
    phone_number = models.CharField(max_length=15)  # Tambahkan field untuk nomor telepon

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # ID unik untuk setiap pesanan
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Relasi ke model Product (ForeignKey)
    quantity = models.PositiveIntegerField()  # Jumlah produk yang dipesan
    customer_name = models.CharField(max_length=100)  # Nama pemesan
    customer_email = models.EmailField()  # Email pemesan
    address = models.TextField()  # Alamat pengiriman

    @property
    def total_price(self):
        return self.quantity * self.product.price  # Menghitung total harga dari pesanan

    def __str__(self):
        return f'Order by {self.customer_name} for {self.product.name}'  # String representation dari objek pesanan
