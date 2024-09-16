from django.shortcuts import render, redirect
from main.forms import OrderForm
from main.models import Order, Product
from django.http import HttpResponse
from django.core import serializers

def order_gpu(request):
    form = OrderForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "order_form.html", context)

# Create your views here.
def show_main(request):
    form = OrderForm()  # Membuat instance form
    order = Order.objects.all()
    context = {
        'apk' : 'nvloo',
        'name': 'Farrel',
        'class': 'PBP F',
        'order': order,
        'form' : form,
    }

    return render(request, "main.html", context)

def order_success(request):
    return render(request, 'order_success.html')
def show_xml(request):
    data = Order.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = Order.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request, id):
    data = Order.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Order.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")