from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum
import math
import json


import stripe
stripe.api_key = "sk_test_VzjYazjHLjiFmX5MmniSHUVA00Z2zoKNzk"


from .models import ItemPricing, Topping, MenuItems, menuCateg, Items, Orders
# Create your views here.
def index(request):
    context = getMenuData(request)
    return render(request, "menu/index.html", context)
    

def register_page(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username=username, password=password,email=email,first_name=firstname,last_name=lastname, is_staff=True)

        # Create new User in Strip with API
        stripe.Customer.create(
            description="Customer for "+ email,
            name = firstname +" "+lastname,
            email = email,
            source="tok_mastercard" # obtained with Stripe.js
        )

        if user:
            user.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "menu/register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:

            return render(request, "menu/login.html", {"message":"Invalid credentials."})
    else:
        return render(request, "menu/login.html")
def logout_page(request):
    logout(request)
    return render(request, "menu/login.html",)


def getMenuData(request):
    allpizza = MenuItems.objects.all()
    pizzaRegSmPrice = ItemPricing.objects.filter(item_type="r", item_size="s").order_by("item_price")
    pizzaReglgPrice = ItemPricing.objects.filter(item_type="r", item_size="l").order_by("item_price")
    pizazRegPrice = zip(pizzaRegSmPrice, pizzaReglgPrice)
    pizzaSiSmPrice = ItemPricing.objects.filter(item_type="s", item_size="s").order_by("item_price")
    pizzaSilgPrice = ItemPricing.objects.filter(item_type="s", item_size="l").order_by("item_price")
    pizazSiPrice = zip(pizzaSiSmPrice, pizzaSilgPrice)

    toppings = Topping.objects.all()

    menuCategs = menuCateg.objects.all()

    menuItem = Items.objects.all()

    context = {
        "user": request.user,
        "allpizza" :allpizza,
        "pizazRegPrice" : pizazRegPrice,
        "pizazSiPrice" : pizazSiPrice,
        "menuCategs" : menuCategs,
        "menuItems" : menuItem,
    }
    return context

def our_menu(request):

    context = getMenuData(request)

    return render(request, "menu/menu.html", context)



def cart(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    orders = Orders.objects.filter(customer=request.user, finished=False)
    context = {
        "orders" : orders,
        "total" : Orders.objects.filter(customer=request.user, finished=False).aggregate(Sum('subtotal')),

    }
    #     return render(request, "menu/cart.html", context)
    return render(request, "menu/cart.html", context)

def calc_total(request):
    if not request.is_ajax: return { "success": False }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    items = request.POST['items']
    items = json.loads(items)

    date = {}
    for item in items:
        order = Orders.objects.get(pk=int(item['id']))

        order.quantity = item['item_count']
        order.subtotal = item['subtotal']

        order.save()
        total = Orders.objects.filter(customer=request.user, finished=False).aggregate(Sum('subtotal'))
        data = {'item_id': item['id'], "quantity":order.quantity, "subtotal":order.subtotal,"total":total }

    print(data)
    return JsonResponse({"success":True, "data":data })


def changePrice(request):
    if not request.is_ajax: return { "success": False }
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    items = request.POST['items']
    items = json.loads(items)

    date = {}
    for item in items:
        order = Orders.objects.get(pk=int(item['id']))
        print(item['newPrice'])
        order.price = float(item['newPrice'])
        order.subtotal = order.price * order.quantity
        order.save()

        total = Orders.objects.filter(customer=request.user, finished=False).aggregate(Sum('subtotal'))
        data = {'item_id': item['id'], "quantity":order.quantity, "price":order.price, "subtotal":order.subtotal,"total":total }

    print(data)
    return JsonResponse({"success":True, "data":data })


def add2chart(request):
    if not request.is_ajax: return { "success":False }

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    items = request.POST['items']
    items = json.loads(items)

    for item in items:

        print(item['id'])
        get_item = Items.objects.get(pk=int(item['id']))
        customer = request.user
        item_name = get_item
        sm_price = get_item.smPrice
        lg_price = get_item.lgPrice

        if sm_price != 0:
            price = sm_price
        elif  lg_price != 0:
            price = lg_price

        item_categ = get_item.menuCateg
        ordered = True
        finished = False
        quantity = 1
        subtotal = price*quantity
        order = Orders.objects.create(customer=customer, menu=item_categ, item=item_name,ordered=ordered, finished=finished, price=price, quantity=quantity, subtotal=subtotal )
        print(order)
        order.save()

        print(get_item)

    return JsonResponse({"success":True, })

def creatStripeCustomer(request):

    # Create new User in Strip with API
    stripe.Customer.create(
        description="Customer for "+ request.user.email,
        name = request.user.first_name +" "+request.user.last_name,
        email = request.user.email,
        source="tok_mastercard" # obtained with Stripe.js
    )

    return True
def checkout(request):

    orders = Orders.objects.filter(customer=request.user, finished=False)

    total = Orders.objects.filter(customer=request.user, finished=False).aggregate(Sum('subtotal'))

    customers =  stripe.Customer.list(limit=3)
    invoice_item = []

    for customer in customers["data"]:

        if customer["email"] == request.user.email:

            for order in orders:
                item_name = order.item.name
                price_unit = order.price
                quantity = order.quantity
                amount = order.subtotal

                item = stripe.InvoiceItem.create(
                    customer = customer["id"],
                    description = item_name,
                    # amount = int(amount*100),
                    quantity = quantity ,
                    unit_amount_decimal = price_unit*100 , # Decimal Number
                    currency = "usd",

                )
                invoice_item.append(item)
                print(item)

                if item:
                    order.finished = True
                    order.save()

            invoices = stripe.Invoice.create(
                customer = customer["id"],
                collection_method='send_invoice',
                days_until_due=30,
                auto_advance=True

            )
            sendInvoiceViaEmail(invoices["id"])
            print(invoices["id"])

        else:
            print("Your Create A new user in stripe platform")
            creatStripeCustomer(request)

    return HttpResponseRedirect(reverse("mycart"))

def sendInvoiceViaEmail(invoice_id):
    return stripe.Invoice.send_invoice(invoice_id)
