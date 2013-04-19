#View for orders
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from orders.models import Product, Customer, Order
from datetime import date

def orders(request):
  productId = request.POST.get('productId')
  products = Product.objects.filter(id=productId)
  return render_to_response('orders/orders.html',{'products':products, 'id':productId},RequestContext(request))
  

def transaction(request):
  expiration=request.POST.get('expiration')
  customer = Customer(
    fullname=request.POST.get('fullname'),
    
    shipAddress=request.POST.get('ship_address'),
    shipCity=request.POST.get('ship_city'),
    shipState=request.POST.get('ship_state'),
    shipZip=request.POST.get('ship_zip'),
    
    billAddress=request.POST.get('bill_address'),
    billCity=request.POST.get('bill_city'),
    billState=request.POST.get('bill_state'),
    billZip=request.POST.get('bill_zip'),
    
    card_no=request.POST.get('card_no'),
    exp_month=str(expiration[5:]),
    exp_year=str(expiration[:4]),
    cvv=request.POST.get('cvv'),
  )
  customer.save()
  productId = request.POST.get('product_id')
  customerId = customer.id
  products = Product.objects.get(pk=productId)
  customers = Customer.objects.get(pk=customerId)
  order = Order(
    product_name=products,
    customers=customers,
    payment_amount=products.price,
  )
  order.save()
  data={
    'orders': orders,
    'customers': customers,
    'products': products.price,
    'date':date.today()
  }
  return render_to_response('orders/transactions.html',data,RequestContext(request))
  #return redirect('/',data)
  
  
def confirmation(request):
  return HttpResponse("Hello Again!")
  
  
  
  
  