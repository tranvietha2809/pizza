from django.contrib import admin
from .models import *
# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    list_display = ("__str__", "pizza_price",)

class PastaAdmin(admin.ModelAdmin):
    list_display = ("__str__", "pasta_price",)

class SubsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "subs_price",)

class SaladsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "salads_price",)

class DinnerPlattersAdmin(admin.ModelAdmin):
    list_display = ("platters", "platters_price",)

class PizzaOrderAdmin(admin.ModelAdmin):
    list_display = ("get_user", "pizza", "toppings_1", "toppings_2", "toppings_3", "get_address",)
    
    def get_user(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.user
    
    get_user.short_description = "User"
    get_user.admin_order_field = "cart__user"

    def get_address(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.address
    get_address.short_description = "Address"
    get_address.admin_order_field = "cart__address"


class PlattersOrderAdmin(admin.ModelAdmin):
    list_display = ("get_user", "platters", "get_address","complete",)
    
    def get_user(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.user
    
    get_user.short_description = "User"
    get_user.admin_order_field = "cart__user"

    def get_address(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.address
    get_address.short_description = "Address"
    get_address.admin_order_field = "cart__address"

class PastaOrderAdmin(admin.ModelAdmin):
    list_display = ("get_user", "pasta", "get_address","complete",)
    
    def get_user(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.user
    
    get_user.short_description = "User"
    get_user.admin_order_field = "cart__user"

    def get_address(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.address
    get_address.short_description = "Address"
    get_address.admin_order_field = "cart__address"

class SubsOrderAdmin(admin.ModelAdmin):
    list_display = ("get_user", "subs", "get_condiments", "extra_cheese", "get_address","complete",)
    
    def get_user(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.user
    
    get_user.short_description = "User"
    get_user.admin_order_field = "cart__user"

    def get_address(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.address
    get_address.short_description = "Address"
    get_address.admin_order_field = "cart__address"

    SubsOrder.get_condiments.short_description = "Condiments"

class SaladsOrderAdmin(admin.ModelAdmin):
    list_display = ("get_user", "salads", "get_address","complete",)
    
    def get_user(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.user
    
    get_user.short_description = "User"
    get_user.admin_order_field = "cart__user"

    def get_address(self, obj):
    ##################################
    #   Method to add foreign key of object to admin interface
    #   Params:
    #       obj: the current object of the Admin interface
    #   Return: 
    #       The foreign key
    ##################################
        return obj.cart.address
    get_address.short_description = "Address"
    get_address.admin_order_field = "cart__address"

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pasta, PastaAdmin)
admin.site.register(Subs, SubsAdmin)
admin.site.register(Salads, SaladsAdmin)
admin.site.register(Toppings)
admin.site.register(Condiments)
admin.site.register(DinnerPlatters)
admin.site.register(Cart)

admin.site.register(TypeID_subs)
admin.site.register(PizzaOrder, PizzaOrderAdmin)
admin.site.register(PastaOrder, PastaOrderAdmin)
admin.site.register(SubsOrder, SubsOrderAdmin)
admin.site.register(SaladsOrder, SaladsOrderAdmin)
admin.site.register(PlattersOrder, PlattersOrderAdmin)

admin.site.register(DiscountCode)