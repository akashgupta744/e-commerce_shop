from django import template

register = template.Library()

@register.filter
def get_value_for_product(dictionary, key):
    return dictionary.get(key, 0)

@register.filter(name='currency')
def currency(number):
    return " ₹ "+ str(number)

@register.filter(name='multiply')
def multiply(number , number1):
    return number * number1

