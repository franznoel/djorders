# Index Page

from django.conf.urls import patterns, url
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from orders.models import Product
from django.shortcuts import render_to_response

from django.conf import settings

def home(request):
  products = Product.objects.all()
  return render_to_response('djorders/index.html',{'products':products},RequestContext(request))
  #return HttpResponse(template.render(context))
