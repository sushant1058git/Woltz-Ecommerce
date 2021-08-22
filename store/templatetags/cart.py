from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return True

    return False


@register.filter(name='quantity')
def quantity(product, cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return cart.get(key)

    return 0


@register.filter(name='currency')
def rs_sign(number):
    return "₹ " + str(number)


@register.filter(name='total_cart_quantity')
def total_cart_quantity(cart):
    values = cart.values()
    total = sum(values)
    return total


@register.filter(name='total_price')
def total_price(product, cart):
    return product.price * quantity(product, cart)


@register.filter(name="cart_total")
def cart_total(products, cart):
    sum = 0
    for product in products:
        sum += total_price(product, cart)

    return sum
