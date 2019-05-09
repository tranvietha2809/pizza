from decimal import Decimal

def valid_subs(subs, condiments):
    ##################################
    #   Method to validate condiments of a subs
    #   Args:
    #   - subs = a subs objects
    #   - condiments= list contain condiments
    #   Return: 
    #   - Corrected condimnets (in case subs doesn't allow condiments)
    ##################################
    if not subs.subs_type.can_add_condiments:
        condiments = ['none']
    return condiments

def subs_pricing(subs, condiments, extra_cheese):
    ##################################
    #   Method to get price of a subs
    #   Args:
    #   - subs = a subs objects
    #   - condiments= list contain condiments
    #   = extra_cheese= boolean variable 
    #   Return: 
    #   - subs price
    ##################################
    base_price = subs.subs_price
    if extra_cheese:
        base_price += Decimal(0.5)
    if condiments is not None:
        for condiment in condiments:
            if condiment == "none":
                continue
            else:
                base_price += Decimal(0.5)
    return base_price