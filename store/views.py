from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json

# Create your views here.
# view for the all products page / home page
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
        items = order.orderitem_set.all()
        cartitem = order.cart_item
        name = customer.name
    else:
        items = []
        order = {'cart_item': 0, 'cart_total': 0}
        cartitem = order['cart_item']
        name = 'Anonymous'
    
    products = Product.objects.all()
    context = {'products': products, 'cartitem': cartitem, 'name': name}
    return render(request, 'store/index.html', context)

# view for the shopping cart page
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
        items = order.orderitem_set.all()
        cartitem = order.cart_item
        name = customer.name
    else:
        items = []
        order = {'cart_item': 0, 'cart_total': 0}
        cartitem = order['cart_item']
        name = 'Anonymous'

    context = {'items': items, 'order': order, 'cartitem': cartitem, 'name': name}
    return render(request, 'store/cart.html', context)

# view for the product detail page
def product_detail(request, id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer)
        items = order.orderitem_set.all()
        cartitem = order.cart_item
        name = customer.name
    else:
        items = []
        order = {'cart_item': 0, 'cart_total': 0}
        cartitem = order['cart_item']
        name = 'Anonymous'
    product = Product.objects.get(id = id)
    context = {'product': product, 'cartitem': cartitem, 'name': name}
    return render(request, 'store/product.html', context)

def addItem(request):
    data = json.loads(request.body)
    productid = data['productid']
    action = data['action']
    customer = request.user.customer
    product = Product.objects.get(id = productid)
    order, created = Order.objects.get_or_create(customer = customer)
    orderitem, created = OrderItem.objects.get_or_create(order = order, product = product)

    if action == 'add':
        orderitem.quantity += 1
    elif action == 'remove':
        orderitem.quantity -= 1
    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse('Successfully added the item', safe=False)

