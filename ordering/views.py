from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
import json
from .helpers import *
from .models import *
from .forms import *

# Create your views here.
@login_required
def index(request):
    ##################################
    #   The main page. 
    #   Before loading will check if user has active cart or create new cart if none is active
    ##################################
    try:
        active_cart = Cart.objects.get(
            user=request.user,
            active=True
            )
        request.session.cart = active_cart
    except ObjectDoesNotExist:
        active_cart = Cart.objects.create(
            user=request.user
        )
    request.session["cart"] = active_cart.id
    return render(request, "index/index.html", {
        "user": request.user
        })

@login_required
def pizza(request):
    pizza_form = PizzaForm()
    context = {
        "form": pizza_form
    }
    return render(request, "pizza/pizza.html", context=context)

@login_required
def get_pizza_price(request):
    if request.is_ajax():
        try:
            base = request.GET.get('base')
            type = request.GET.get('type')
            size = request.GET.get('size')
            price = Pizza.objects.get(base__base=base, pizza_type__type=type, pizza_size__size=size).pizza_price
            data = {
                "price": price
            }
        except ObjectDoesNotExist:
            data = {
                "header": 500,
                "message": "oops something is wrong with our server!. Try again :("
            }
        return JsonResponse(data)
    else: 
        return redirect(reverse("ordering:pizza"))

@login_required
def add_pizza(request):
    if request.method == "POST":
        pizza_order_form = PizzaForm(request.POST)
        if pizza_order_form.is_valid():
            pizza_base = pizza_order_form.cleaned_data["base"]
            pizza_size = pizza_order_form.cleaned_data["size"]
            pizza_type = pizza_order_form.cleaned_data["type"]
            toppings_1 = pizza_order_form.cleaned_data["toppings_1"]
            toppings_2 = pizza_order_form.cleaned_data["toppings_2"]
            toppings_3 = pizza_order_form.cleaned_data["toppings_3"]
            try:
                user_pizza = Pizza.objects.get(
                    base__base=pizza_base,
                    pizza_size__size=pizza_size,
                    pizza_type__type=pizza_type
                )
                PizzaOrder.objects.create(
                    pizza=user_pizza,
                    cart=Cart.objects.get(id=request.session["cart"]),
                    toppings_1=Toppings.objects.get(topping=toppings_1),
                    toppings_2=Toppings.objects.get(topping=toppings_2),
                    toppings_3=Toppings.objects.get(topping=toppings_3),
                    price=user_pizza.pizza_price
                )
                return redirect(reverse("ordering:pizza"))
            except ObjectDoesNotExist:
                return HttpResponseBadRequest(content="Something's wrong :(")
    else:
        return redirect(reverse("ordering:pizza"))

@login_required
def subs(request):
    subs_form = SubsForm()
    context = {
        "form" : subs_form
    }
    return render(request, "subs/subs.html", context=context)


@login_required
def add_subs(request):
    if request.method == "POST":
        subs_order_form = SubsForm(request.POST)
        if subs_order_form.is_valid():
            subs_type = subs_order_form.cleaned_data["subs_type"]
            subs_size = subs_order_form.cleaned_data["subs_size"]
            condiments = request.POST.getlist('condiments')
            extra_cheese = subs_order_form.cleaned_data['extra_cheese']
            try:
                current_subs = Subs.objects.get(
                    subs_size__size=subs_size,
                    subs_type__type=subs_type
                )
                condiments = valid_subs(current_subs, condiments)
                price = subs_pricing(current_subs, condiments, extra_cheese)
                subs_order = SubsOrder.objects.create(
                    subs=current_subs,
                    cart=Cart.objects.get(id=request.session['cart']),
                    extra_cheese=extra_cheese,
                    price=price
                )
                for condiment in condiments:
                    subs_order.condiments.add(Condiments.objects.get(condiment=condiment))
                return redirect(reverse("ordering:subs"))
            except ObjectDoesNotExist:
                return HttpResponseBadRequest(content="Something's wrong :(")
    else:
        return redirect(reverse("ordering:subs"))

@login_required
def get_subs_price(request):
    if request.is_ajax():
        try:
            subs_type = request.GET.get('subs_type')
            subs_size = request.GET.get('subs_size')
            condiments = request.GET.getlist('condiments[]')
            extra_cheese = json.loads(request.GET.get('extra_cheese'))
            current_subs = Subs.objects.get(
                    subs_size__size=subs_size,
                    subs_type__type=subs_type
                )
            price = subs_pricing(current_subs, condiments, extra_cheese)
            data = {
                "price": price
            }
        except ObjectDoesNotExist:
            data = {
                "header": 500,
                "message": "oops something is wrong with our server!. Try again :("
            }
        return JsonResponse(data)
    else: 
        return redirect(reverse("ordering:subs"))

@login_required
def salads(request):
    salads_form = SaladsForm()
    context = {
        "form": salads_form
    }
    return render(request, "salads/salads.html", context=context)

@login_required
def add_salads(request):
    if request.method == "POST":
        salads_order_form = SaladsForm(request.POST)
        if salads_order_form.is_valid():
            salads_type = request.POST["salads_type"]
            try:
                current_salads = Salads.objects.get(
                    salads_type__type=salads_type
                )
                SaladsOrder.objects.create(
                    salads=current_salads,
                    cart=Cart.objects.get(id=request.session['cart']),
                    price=current_salads.price
                )
                return redirect(reverse("ordering:salads"))
            except ObjectDoesNotExist:
                return HttpResponseBadRequest(content="Something's wrong :(")
    else:
        return redirect(reverse("ordering:salads"))

@login_required
def get_salads_price(request):
    if request.is_ajax():
        try:
            salads_type = request.GET.get('salads_type')
            current_salads = Salads.objects.get(
                salads_type__type=salads_type
            )
            price = current_salads.price
            data = {
                "price": price
            }
        except ObjectDoesNotExist:
            data = {
                "header": 500,
                "message": "oops something is wrong with our server!. Try again :("
            }
        return JsonResponse(data)
    else: 
        return redirect(reverse("ordering:salads"))

@login_required
def platters(request):
    platters_form = PlattersForm()
    context = {
        "form": platters_form
    }
    return render(request, "platters/platters.html", context=context)

@login_required
def add_platters(request):
    if request.method == "POST":
        platters_form = PlattersForm(request.POST)
        if platters_form.is_valid():
            platters_size = request.POST["platters_size"]
            platters_type = request.POST["platters_type"]
            try:
                current_platters = DinnerPlatters.objects.get(
                    platters_size__size=platters_size,
                    platters_type__type=platters_type
                )
                PlattersOrder.objects.create(
                    platters=current_platters,
                    cart=Cart.objects.get(id=request.session['cart']),
                    price=current_platters.price
                )
                return redirect(reverse("ordering:platters"))
            except ObjectDoesNotExist:
                return HttpResponseBadRequest(content="Something's wrong :(")
    else:
        return redirect(reverse("ordering:platters"))

@login_required
def get_platters_price(request):
    if request.is_ajax():
        try:
            platters_size = request.GET.get('platters_size')
            platters_type = request.GET.get('platters_type')
            current_platters = DinnerPlatters.objects.get(
                plattters_size__size=platters_size,
                platters_type__type=platters_type
            )
            price = current_platters.price
            data = {
                "price": price
            }
        except ObjectDoesNotExist:
            data = {
                "header": 500,
                "message": "oops something is wrong with our server!. Try again :("
            }
        return JsonResponse(data)
    else: 
        return redirect(reverse("ordering:platters"))