from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='img/',null=True)

    def __str__(self) -> str:
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def cart_total(self):
        orderitems = self.orderitem_set.all()
        return sum([item.cal_total for item in orderitems])
    
    @property
    def cart_item(self):
        orderitems = self.orderitem_set.all()
        return sum([item.quantity for item in orderitems])

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True)
    date_order = models.DateTimeField(auto_now_add=True)

    @property
    def cal_total(self):
        return self.product.price * self.quantity
        