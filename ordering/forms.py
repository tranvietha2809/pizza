from django import forms
from .models import *

class PizzaForm(forms.Form):
    base = forms.ChoiceField(choices=[
            (base, base) for base in 
            list(BaseID.objects.values_list('base', flat=True))
        ])

    size = forms.ChoiceField(choices=[
            (size, size) for size in 
            list(SizeID.objects.values_list('size', flat=True))
        ])

    type = forms.ChoiceField(choices=[
            (type, type) for type in 
            list(TypeID.objects.values_list('type', flat=True))
        ])

    toppings_1 = forms.ChoiceField(choices=[
            (topping, topping) for topping in 
            list(Toppings.objects.values_list('topping', flat=True)) 
        ], initial="none")

    toppings_2 = forms.ChoiceField(choices=[
            (topping, topping) for topping in 
            list(Toppings.objects.values_list('topping', flat=True)) 
        ], initial="none")

    toppings_3 = forms.ChoiceField(choices=[
            (topping, topping) for topping in 
            list(Toppings.objects.values_list('topping', flat=True)) 
        ], initial="none")
        
    class Media:
        css = ("css/ordering/pizza/pizza.css")
        js = ("js/ordering/pizza/pizza.js")

class SubsForm(forms.Form):
    subs_size = forms.ChoiceField(choices=[
        (size, size) for size in
        list(SizeID.objects.values_list('size', flat=True))
    ])
    subs_type = forms.ChoiceField(choices=[
        (type, type) for type in
        list(TypeID_subs.objects.values_list('type', flat=True))
    ])
    condiments = forms.MultipleChoiceField(choices=[
        (condiments, condiments) for condiments in
        list(Condiments.objects.values_list('condiment', flat=True))
    ], widget=forms.CheckboxSelectMultiple(), required = False)
    extra_cheese = forms.BooleanField(required=False)
    class Media:
        css = ("css/ordering/subs/subs.css")
        js = ("js/ordering/subs/subs.js")

class SaladsForm(forms.Form):
    salads_type = forms.ChoiceField(choices=[
        (type, type) for type in
        list(TypeID_salads.objects.values_list('salads_type', flat=True))
    ])
    class Media:
        css = ("css/ordering/salads/salads.css")
        js = ("js/ordering/salads/salads.js")


class PlattersForm(forms.Form):
    platters_size = forms.ChoiceField(choices=[
        (size, size) for size in
        list(SizeID.objects.values_list('size', flat=True))
    ])
    platters_type = forms.ChoiceField(choices=[
        (type, type) for type in
        list(TypeID_platters.objects.values_list('platters_type', flat=True))
    ])
    class Media:
        css = ("css/ordering/platters/platters.css")
        js = ("js/ordering/platters/platters.js")
