from django.shortcuts import render, redirect, get_object_or_404, reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json

# Fungsi untuk menambah produk via halaman biasa (non-AJAX)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Mengaitkan produk dengan user yang login
            product.save()
            return redirect('main:show_main')  # Redirect ke halaman utama setelah berhasil menambah produk
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

# Fungsi untuk menambah produk via AJAX
@csrf_exempt
@require_POST
def add_product_ajax(request):
    try:
        data = json.loads(request.body.decode('utf-8'))

        # Membersihkan dan memvalidasi input dari pengguna
        product_name = strip_tags(data.get('name', '').strip())
        price = data.get('price')
        description = strip_tags(data.get('description', '').strip())

        # Validasi jika ada field yang kosong
        if not product_name or not price or not description:
            return JsonResponse({"error": "Semua field harus diisi!"}, status=400)

        # Validasi harga agar merupakan angka positif
        try:
            price = float(price)
            if price <= 0:
                return JsonResponse({"error": "Harga harus lebih dari 0."}, status=400)
        except ValueError:
            return JsonResponse({"error": "Harga tidak valid."}, status=400)

        # Membuat produk baru dan menyimpannya ke database
        new_product = Product(
            name=product_name,
            price=price,
            description=description,
            user=request.user  # Mengaitkan produk dengan user yang login
        )
        new_product.save()

        # Mengembalikan respon sukses dalam format JSON
        return JsonResponse({
            "message": "Produk berhasil ditambahkan!",
            "product": {
                "id": str(new_product.id),
                "name": new_product.name,
                "price": new_product.price,
                "description": new_product.description
            }
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({"error": "Data tidak valid."}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('main:show_main')

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductForm(instance=product)
    
    context = {
        'form': form,
        'product': product,
    }
    
    return render(request, 'edit_product.html', context)

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        product = form.save(commit=False)
        product.user = request.user  # Kaitkan produk dengan user yang login
        product.save()
        return redirect('main:show_main')
    
    user = request.user

    context = {
        'apk' : 'nvloo',
        'name': 'Farrel',
        'class': 'class F',
        'last_login': request.COOKIES['last_login'],
        'user': user,

    }

    return render(request, "main.html", context)

def add_success(request):
    return render(request, 'add_success.html')
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
      else:
        messages.error(request, "Invalid username or password. Please try again.")


   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response