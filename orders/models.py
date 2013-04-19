from django.db import models

class Customer(models.Model):
  fullname = models.CharField(max_length=200)
  
  shipAddress = models.CharField(max_length=200)
  shipCity = models.CharField(max_length=200)
  shipState = models.CharField(max_length=2)
  shipZip = models.CharField(max_length=5)
  
  billAddress = models.CharField(max_length=200)
  billCity = models.CharField(max_length=200)
  billState = models.CharField(max_length=2)
  billZip = models.CharField(max_length=5)

  card_no = models.CharField(max_length=16)
  exp_month = models.CharField(max_length=2)
  exp_year = models.CharField(max_length=4)
  cvv = models.CharField(max_length=4)
  
  def __unicode__(self):
    return self.fullname


class Product(models.Model):
  name = models.CharField(max_length=80)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  cropped_image = models.ImageField(upload_to='/'.join(['static/img/products/cropped']))
  large_image = models.ImageField(upload_to='/'.join(['static/img/products']))
  
  def __unicode__(self):
    return self.name
  

class Order(models.Model):
  product_name = models.ForeignKey(Product)
  customers = models.ForeignKey(Customer)
  payment_amount = models.DecimalField(max_digits=10,decimal_places=2)
  date_ordered = models.DateTimeField('date ordered',auto_now_add=True)
  
  def __unicode__(self):
    return self.product_name


