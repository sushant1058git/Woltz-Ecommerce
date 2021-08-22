from django import template

register = template.Library()


@register.filter(name='multiply')
def mul(n1, n2):
    return n1*n2


@register.filter(name='cart_from_buy_now')
def cart_from_buy_now(product ):
    return product.price

