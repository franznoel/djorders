from django.contrib import admin
from orders.models import Customer, Product, Order

class ProductAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Product Name',{'fields': ['name']}),
    (None,{'fields': ['price']}),
    (None,{'fields': ['cropped_image']}),
    (None,{'fields': ['large_image']}),
  ]
  
  list_display = ('name','price')
  search_fields = ['name']
  list_filter = ['name']

class CustomerAdmin(admin.ModelAdmin):
  fieldsets = [
    ('Full Name',{'fields': ['fullname']}),
    ('Billing',{'fields': ['billAddress']}),
    ('Shipping',{'fields': ['shipAddress']}),
  ]
  
  list_display = ('fullname','billAddress','shipAddress')
  search_fields = ['fullname']
  filter = ['fullname']
  list_filter = ['fullname']

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order)
