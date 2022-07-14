from atexit import register
from django import template

register = template.Library()

@register.simple_tag
def saludar():
    return "Hola a todos, soy un tag"


@register.simple_tag
def saludar_con_nombre(nombre):
    return f"Hola soy {nombre}"

def ejemplo(value, arg):
    if len(value)>0:
        return value
    return arg

register.filter("ejemplo", ejemplo)