from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
import datetime
# Create your tests here.

class ModelTestCases(TestCase):

    #Creating a test user
    def setUp(self):
        self.autoTestUser = User.objects.create_user(
            username="autotestx", 
            first_name="ha", 
            last_name="test", 
            email="abc@ccc.com", 
            password="vhax2019", 
            is_active=True
            )
        self.small = SizeID.objects.create(size="small")
        self.large = SizeID.objects.create(size="large")
        self.regular = BaseID.objects.create(base="regular")
        self.sicilian = BaseID.objects.create(base="sicilian")
        self.cheese = TypeID.objects.create(type="cheese")
        self.two_toppings = TypeID.objects.create(type="two toppings")
        self.three_toppings = TypeID.objects.create(type="three toppings")
        self.special = TypeID.objects.create(type="special")
        self.pepperoni = Toppings.objects.create(topping="pepperoni")
        self.sausage = Toppings.objects.create(topping="sausage")
        self.mushrooms = Toppings.objects.create(topping="mushrooms")

    def test_addItemsToCart(self):
        
        #Creating an order
        RegularSmallCheesePizza = Pizza.objects.create(base=self.regular, pizza_size=self.small, pizza_type=self.cheese, pizza_price=12.20)

        #Creating a cart for user
        testCart = Cart.objects.create(user=self.autoTestUser)

        #Adding item to cart
        testOrder = PizzaOrder.objects.create(pizza= RegularSmallCheesePizza, cart=testCart)
        self.assertEqual(PizzaOrder.objects.all().count(), 1)

        #Adding another item to cart
        testOrder_2 = PizzaOrder.objects.create(pizza= RegularSmallCheesePizza, cart=testCart)
        self.assertEqual(PizzaOrder.objects.all().count(), 2)

        #Adding two different items to cart
        SicilianLargeSpecialPizza = Pizza.objects.create(base=self.sicilian, pizza_size=self.large, pizza_type=self.special, pizza_price=44.70)
        testOrder_3 = PizzaOrder.objects.create(pizza= SicilianLargeSpecialPizza, cart=testCart)
        self.assertEqual(PizzaOrder.objects.filter(cart= testCart).count(), 3)
        self.assertEqual(PizzaOrder.objects.filter(pizza= SicilianLargeSpecialPizza).count(), 1)
        self.assertEqual(PizzaOrder.objects.filter(pizza= RegularSmallCheesePizza).count(), 2)

    def test_creatingPizzaWithManyToppings(self):

        #Creating Pizza with two toppings
        RegularSmallTwoToppingsPizza = Pizza.objects.create(base=self.regular, pizza_size = self.small, pizza_type=self.two_toppings, pizza_price=14.70)
        RegularSmallTwoToppingsPizza.toppings.add(self.sausage)
        RegularSmallTwoToppingsPizza.toppings.add(self.pepperoni)
        self.assertEqual(RegularSmallTwoToppingsPizza.toppings.count(), 2)

        #Creating Pizza with three topppings
        RegularSmallThreeToppingsPizza = Pizza.objects.create(base=self.regular, pizza_size = self.small, pizza_type=self.three_toppings, pizza_price=14.70)
        RegularSmallThreeToppingsPizza.toppings.add(self.sausage)
        RegularSmallThreeToppingsPizza.toppings.add(self.pepperoni)
        RegularSmallThreeToppingsPizza.toppings.add(self.mushrooms)
        self.assertEqual(RegularSmallTwoToppingsPizza.toppings.count(), 2)