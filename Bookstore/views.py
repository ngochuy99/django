import datetime

from django.shortcuts import render, redirect
from Bookstore.form import *
from Bookstore.models import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            customer = Customer.objects.get(username=username, password=password)
            request.session["count"] = 0
            return redirect("/bookstore/index")
        except:
            return render(request, 'bookstore/login.html', {"status": "unset"})
    return render(request, 'bookstore/login.html', {"status": "none"})


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get("firstname", "")
        last_name = request.POST.get("lastname", "")
        password = request.POST.get("password", "")
        re_password = request.POST.get("re_password", "")
        district = request.POST.get("district", "")
        city = request.POST.get("city", "")
        street = request.POST.get("street", "")
        gender = request.POST.get("gender", "male")
        dob = request.POST.get("dob", "")
        tel = request.POST.get("telephone")
        username = request.POST.get("username", "")
        try:
            if username != "" and password == re_password:
                fullname = Fullname(firstname=first_name, lastname=last_name)
                fullname.save()

                address = Address(street=street, district=district, city=city)
                address.save()

                customer = Customer(gender=gender, dob=dob, phone=tel, fullname=fullname, address=address,
                                    username=username,
                                    password=password)
                customer.save()
                return render(request, 'bookstore/login.html', {"status": "none"})
            else:
                if username == "":
                    return render(request, 'bookstore/register.html',
                                  {"message": "username can not be blank", "status": "unset"})
                if password != re_password:
                    return render(request, 'bookstore/register.html',
                                  {"message": "password and repeat password not match", "status": "unset"})
        except:
            pass
            return render(request, 'bookstore/register.html',
                          {"message": "Username has already exists", "status": "unset"})
    return render(request, 'bookstore/register.html', {"status": "none"})


def index(request):
    book = Book.objects.all().order_by("inStock")
    clothe = Clothe.objects.all().order_by("inStock")
    electronic = Electronic.objects.all().order_by("inStock")
    listbook = []
    listelectronic = []
    listclothes = []
    for b in book:

        if b.discount == 0:
            b.discounted = b.price
        else:
            b.discounted = b.discount * b.price / 100
        listbook.append(b)
    for c in clothe:
        if c.discount == 0:
            c.discounted = c.price
        else:
            c.discounted = c.discount * c.price / 100
        listclothes.append(c)
    for e in electronic:
        if e.discount == 0:
            e.discounted = e.price
        else:
            e.discounted = e.discount * e.price / 100
        listelectronic.append(e)
    return render(request, 'bookstore/mainPage.html', {"listbook": listbook,"listelectronics":listelectronic,"listclothes":listclothes})

def getbook(request):
    book = Book.objects.all()
    list = []
    for b in book:

        if b.discount == 0:
            b.discounted = b.price
        else:
            b.discounted = b.discount * b.price / 100
        list.append(b)
    return render(request, 'bookstore/book.html', {"list": list})

def getElectronics(request):
    electronics = Electronic.objects.all()
    list = []
    for e in electronics:

        if e.discount == 0:
            e.discounted = e.price
        else:
            e.discounted = e.discount * e.price / 100
        list.append(e)
    return render(request, 'bookstore/electronics.html', {"list": list})

def getClothes(request):
    clothes = Clothe.objects.all()
    list = []
    for c in clothes:

        if c.discount == 0:
            c.discounted = c.price
        else:
            c.discounted = c.discount * c.price / 100
        list.append(c)
    return render(request, 'bookstore/clothes.html', {"list": list})

def addcart(request, type , id):
    if type not in request.session:
        request.session[type] = []
    list = request.session.get(type)
    list.append(id)
    request.session[type] = list
    print(list)
    return redirect("/bookstore/"+type)


def addtocart(request, type , id):
    if type not in request.session:
        request.session[type] = []
    list = request.session.get(type)
    list.append(id)
    request.session[type] = list
    print(list)
    return redirect("/bookstore/index")