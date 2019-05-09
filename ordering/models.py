from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
# Create your models here.

# Shared model
class SizeID(models.Model):
    size = models.CharField(max_length=10)
    def __str__(self):
        return f"ID: {self.id} - {self.size}"

class DiscountCode(models.Model):
    discount_code = models.CharField(max_length=10)
    def __str__(self):
        return f"{self.discount_code}"

#Pizza model
class BaseID(models.Model):
    base = models.CharField(max_length=15)
    def __str__(self):
        return f"ID: {self.id} - {self.base}"

class TypeID(models.Model):
    type = models.CharField(max_length=32)
    def __str__(self):
        return f"ID: {self.id} - {self.type}"

class Toppings(models.Model):
    topping = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.topping}"

# Subs model
class Condiments(models.Model):
    condiment = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.condiment}"

class TypeID_subs(models.Model):
    type = models.CharField(max_length=32)
    can_add_condiments = models.BooleanField(default=False)
    def __str__(self):
        return f"ID: {self.id} - {self.type}"

# Pasta model
class TypeID_pasta(models.Model):
    type = models.CharField(max_length=32)   
    def __str__(self):
        return f"ID: {self.id} - {self.type}"

# Salads model
class TypeID_salads(models.Model):
    type = models.CharField(max_length=32)   
    def __str__(self):
        return f"ID: {self.id} - {self.type}"

# Patters model
class TypeID_platters(models.Model):
    type = models.CharField(max_length=32)   
    def __str__(self):
        return f"ID: {self.id} - {self.type}"

class Pizza(models.Model):
    base = models.ForeignKey(BaseID, on_delete=models.CASCADE, related_name="pizza_base")
    pizza_size = models.ForeignKey(SizeID, on_delete=models.CASCADE, related_name="pizza_size")
    pizza_type = models.ForeignKey(TypeID, on_delete=models.CASCADE, related_name="pizza_type")
    pizza_price = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.base.base} {self.pizza_size.size} {self.pizza_type.type}"

class Subs(models.Model):
    subs_size = models.ForeignKey(SizeID, on_delete=models.CASCADE, related_name="subs_size")
    subs_type = models.ForeignKey(TypeID_subs, on_delete=models.CASCADE, related_name="subs_type")
    subs_price = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.subs_size.size} {self.subs_type.type}"

class Pasta(models.Model):
    pasta_type = models.ForeignKey(TypeID_pasta, on_delete=models.CASCADE, related_name="pasta_type")
    pasta_price = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.pasta_type}"


class Salads(models.Model):
    salads_type = models.ForeignKey(TypeID_salads, on_delete=models.CASCADE, related_name="salads_type")
    salads_price = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.salads_type}"
    

class DinnerPlatters(models.Model):
    platters_size = models.ForeignKey(SizeID, on_delete=models.CASCADE, related_name="platters_size")
    platters_type = models.ForeignKey(TypeID_platters, on_delete=models.CASCADE, related_name="platters_type")
    platters_price = models.DecimalField(decimal_places=2, max_digits=4)
    def __str__(self):
        return f"{self.platters_size.size} {self.platters_type}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    cart_date = models.DateField(auto_now_add=True)
    address = models.TextField(null=True)
    def __str__(self):
        return f"{self.id}. user: {self.user} Active: {self.active} Created: {self.cart_date}"
    

class SubsOrder(models.Model):
    subs = models.ForeignKey(Subs, on_delete=models.CASCADE, related_name="subs_types")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="subs_order")
    condiments = models.ManyToManyField(Condiments, blank=True, related_name="subs_condiments")
    extra_cheese = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=Decimal('0.00'))
    def get_condiments(self):
    ##################################
    #   Method to get all condiments of the subs
    #   Return: 
    #       String contains all toppings
    ##################################
        condiments_string = ""
        condiments = self.condiments.all()
        for i in range(condiments.count()):
            condiments_string += str(condiments[i])
            if i < condiments.count()-1:
                condiments_string += ", "
        return condiments_string
    
    def __str__(self):
        return f"{self.cart.user.username} {self.subs.subs_type} with {self.condiments} - {self.cart.address}"

class PastaOrder(models.Model):
    pasta = models.ForeignKey(Pasta, on_delete=models.CASCADE, related_name="pasta_types")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="pasta_cart_order")
    complete = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=Decimal('0.00'))
    def __str__(self):
        return f"{self.cart.user.username} {self.pasta.pasta_type}- {self.cart.address}"


class SaladsOrder(models.Model):
    salads = models.ForeignKey(Salads, on_delete=models.CASCADE, related_name="salads_types")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="salads_cart_order")
    complete = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=Decimal('0.00'))
    def __str__(self):
        return f"{self.cart.user.username} {self.salads.salads_type} - {self.cart.address}"


class PlattersOrder(models.Model):
    platters = models.ForeignKey(DinnerPlatters, on_delete=models.CASCADE, related_name="platters_types")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="platters_cart_order")
    complete = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=Decimal('0.00'))
    def __str__(self):
        return f"{self.cart.user.username} {self.platters.platters_type} - {self.cart.address}"

def none_toppings():
    return Toppings.objects.get(topping='none').id

class PizzaOrder(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_types")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="pizza_cart_order")
    toppings_1 = models.ForeignKey(Toppings, default=none_toppings(), on_delete=models.CASCADE, related_name="toppings_1")
    toppings_2 = models.ForeignKey(Toppings, default=none_toppings(), on_delete=models.CASCADE, related_name="toppings_2")
    toppings_3 = models.ForeignKey(Toppings, default=none_toppings(), on_delete=models.CASCADE, related_name="toppings_3")
    complete = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=Decimal('0.00'))
    def __str__(self):
        return f"{self.cart.user.username} {self.pizza} with {self.toppings_1}, {self.toppings_2}, {self.toppings_3} - {self.cart.address}"


