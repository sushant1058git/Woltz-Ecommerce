from django.contrib import messages
from django.shortcuts import render, redirect
from .models.products import Products
from .models.category import Category
from .models.address import Address
from .models.orders import Orders
from .models import Customers
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password


def index(request):
    if request.method == 'GET':
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = None
        category = Category.get_all_categories()
        categories_Id = request.GET.get('category')

        if categories_Id:
            product = Products.get_all_category_by_id(categories_Id)

        elif 'searched' in request.GET:
            searched = request.GET['searched']
            product = Products.objects.filter(name__icontains=searched)

        else:
            product = Products.get_all_product()

        data = {}
        data['category'] = category
        data['product'] = product

        return render(request, 'index.html', data)

    else:
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)  # The get() method returns the value of the item with the specified key.
            if quantity:
                cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1

        else:
            cart = {}
            cart[product_id] = 1

        request.session['cart'] = cart
        # print(cart)

        return redirect('index')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(email, password)
        customer = Customers.get_customer_by_email(email)
        # print(customer.id)

        if customer:
            if check_password(password, customer.password):
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email  # not necessary
                request.session['name'] = customer.name  # not necessary
                # print(customer.name)
                return redirect(index)
            else:
                msg = "Please check your password"
        else:
            msg = "We cannot find an account with that email address"
    return render(request, 'login.html', {'error': msg})


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    else:
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = Customers(name=name, mobile_number=mobile,
                             email=email, password=password)

        # Password Hashing
        customer.password = make_password(customer.password)

        # password validation

        error_msg = ''

        if len(password) < 6:
            error_msg = 'Passwords must be at least 6 characters..'

        elif customer.isExists(email):
            error_msg = 'User already registered'
        else:
            customer.save()
            messages.success(request, "Account created successfully")
            return redirect('login')

        values_filled = {
            'error': error_msg
        }

    return render(request, 'signup.html', values_filled)


def logout(request):
    request.session.clear()
    return redirect('login')


def cart(request):
    ids = list(request.session.get('cart').keys())
    products = Products.get_product_by_id(ids)
    if request.method == 'GET':
        cart = request.session.get('cart')
        customer = request.session.get('customer_id')

        if cart == {}:
            if customer:
                return render(request, 'empty_customer_cart.html')
            else:
                return render(request, 'empty_cart.html')



        else:
            ids = list(request.session.get('cart').keys())
            products = Products.get_product_by_id(ids)
            return render(request, 'cart.html', {'products': products})

    else:
        print(request.method)
        product_id = request.POST.get('delete')
        print(product_id)
        # product = Products.get_product_by_id(product_id)
        # print(product)
        cart = request.session.get('cart')
        print(cart)
        quantity = cart.get(product_id)
        print(quantity)

        if quantity >=1:
            cart[product_id] = quantity - 1
            # print(quantity)
            request.session['cart'] = cart
            return render(request, 'cart.html', {'products': products})


        elif quantity == 0:
            del cart[product_id]                    ###  or cart.pop(product_id,quantity)
            request.session['cart'] = cart
            print(cart)
            return render(request, 'cart.html', {'products': products})


        elif cart == {}:
            return render(request, 'empty_customer_cart.html')

    return render(request, 'cart.html', {'products': products})


def address(request):
    print(request.method)
    customer = request.session.get('customer_id')
    add = Address.get_address_by_customer_id(customer)
    if request.method == 'GET':

        return render(request, 'address.html', {'add': add})

    else:
        customer = request.session.get('customer_id')
        add = Address.get_address_by_customer_id(customer)
        delete_address = request.POST.get('delete_address')
        address_to_be_deleted = Address.get_address_by_id(delete_address)
        edit_address = request.POST.get('edit_address')
        address_to_be_edited = Address.get_address_by_id(edit_address)

        if customer:
            if address_to_be_deleted:
                address_to_be_deleted.delete()
            return render(request, 'address.html', {'add': add})

        else:
            return redirect(login)


def address_list(request):
    # if request == 'GET':
    customer = request.session.get('customer_id')
    address = Address.get_address_by_customer_id(customer)
    delete_address = request.POST.get('delete_address')
    address_to_be_deleted = Address.get_address_by_id(delete_address)

    if not address:
        return redirect(add_address)
    else:
        address_to_be_deleted.delete()
        return render(request, 'address_list.html', {'address': address})


def review_order(request):
    if request.method == 'GET':
        request.session.clear()
        return render(request, 'login.html')
    else:
        customer = request.session.get('customer_id')
        address_id = request.POST.get('address_id')
        current_address = Address.get_address_by_id(address_id)
        product_id = list(request.session.get('cart').keys())
        products = Products.get_product_by_id(product_id)

        if address_id:

            data = {
                'current_address': current_address,
                'products': products,
            }
            return render(request, 'review_order.html', data)
        else:
            full_name = request.POST.get('full_name')
            mobile = request.POST.get('mobile')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            pin = request.POST.get('pin')

            # print(full_name, address, mobile, city, state, pin)

            address_details = Address(customer=Customers(id=customer),
                                      full_name=full_name,
                                      mobile=mobile,
                                      address=address,
                                      city=city,
                                      state=state,
                                      pin=pin)

            current_address = address_details
            current_address.save()
            data = {
                'current_address': current_address,
                'products': products,
            }
            # print(current_address)
            return render(request, 'review_order.html', data)


def order(request):
    # this is always a POSt request

    customer = request.session.get('customer_id')
    customer_details = list(Customers.get_customer_by_id(customer))
    cart = request.session.get('cart')
    keys = list(cart.keys())
    products = Products.get_product_by_id(keys)

    address_id = request.POST.get('order_id')
    address = Address.get_address_by_id(address_id)

    for add in address:
        for product in products:
            order = Orders(product=product,
                           price=product.price,
                           customer=Customers(id=customer),
                           quantity=cart.get(str(product.id)),
                           address=add.address,
                           mobile=add.mobile)

            order.save()
    request.session['cart'] = {}
    return redirect(thankyou)


def thankyou(request):
    return render(request, 'thankyou.html')


def order_list(request):
    if request.method == 'GET':
        customer = request.session.get('customer_id')
        order = Orders.get_order_by_customerId(customer)

        # print(order.price)

        return render(request, 'order_list.html', {'order': order})


def add_address(request):
    customer = request.session.get('customer_id')
    print(request.method)
    if request.method == 'GET':
        return render(request, 'add_address.html')
    else:
        full_name = request.POST.get('full_name')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')

        print(full_name, address, mobile, city, state, pin)

        address_details = Address(customer=Customers(id=customer),
                                  full_name=full_name,
                                  mobile=mobile,
                                  address=address,
                                  city=city,
                                  state=state,
                                  pin=pin)

        #
        #
        address_details.save()
        messages.success(request, "address added successfully !!")

    return render(request, 'add_address.html')
