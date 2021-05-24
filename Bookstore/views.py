from django.shortcuts import render, redirect

from Bookstore.models import *


# Create your views here.
def login(request):
    if request.method == 'POST':
        try:
            username = request.POST.get("username", "")
            password = request.POST.get("password", "")
            customer = Customer.objects.get(username=username, password=password)
            request.session["username"] = customer.username
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
    return render(request, 'bookstore/mainPage.html',
                  {"listbook": listbook, "listelectronics": listelectronic, "listclothes": listclothes})


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


def addcart(request, type, id):
    if type not in request.session:
        request.session[type] = []
    if "count" not in request.session:
        request.session["count"] = 0
    list = request.session.get(type)
    list.append(id)
    request.session[type] = list
    count = request.session.get("count")
    count += 1
    request.session["count"] = count
    return redirect("/bookstore/" + type)


def addtocart(request, type, id):
    print(type)
    if type not in request.session:
        request.session[type] = []
    if "count" not in request.session:
        request.session["count"] = 0
    list = request.session.get(type)
    list.append(id)
    request.session[type] = list
    count = request.session.get("count")
    count += 1
    request.session["count"] = count
    return redirect("/bookstore/index")


def pay(request):
    if "count" not in request.session:
        request.session["count"] = 0
    booklist = request.session.get("book")
    clotheList = request.session.get("clothes")
    electronicsList = request.session.get("electronics")
    username = request.session.get("username")
    customer = Customer.objects.get(username=username)
    address = customer.address.street + ", " + customer.address.district + ", " + customer.address.city
    listitem = []
    total = 0
    for b in booklist:
        book = Book.objects.get(pk=b)
        if book.discount == 0:
            book.discounted = book.price
        else:
            book.discounted = book.discount * book.price / 100
        total += book.discounted
        listitem.append(book)
    for c in clotheList:
        clothes = Clothe.objects.get(pk=c)
        if clothes.discount == 0:
            clothes.discounted = clothes.price
        else:
            clothes.discounted = clothes.discount * clothes.price / 100
        total += clothes.discounted
        listitem.append(clothes)
    for e in electronicsList:
        electronics = Electronic.objects.get(pk=e)
        if electronics.discount == 0:
            electronics.discounted = electronics.price
        else:
            electronics.discounted = electronics.discount * electronics.price / 100
        total += electronics.discounted
        listitem.append(electronics)
    count = request.session.get("count")
    total += 50000
    request.session["total"] = total
    return render(request, 'bookstore/cart.html',
                  {"count": count, "list": listitem, "total": total, "customer": customer, "address": address})


def saveorder(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        email = request.POST.get("email")
        address = request.POST.get("address")
        customer = Customer.objects.get(username=request.session.get("username"))
        shipment = Shipment(shipper="J&TExpress", destination=address, fee=50000)
        shipment.save()
        order = Order(orderName=firstName + " " + lastName, orderEmail=email, quantity=request.session.get("count"),
                      total=request.session.get("total"), customer=customer, shipment=shipment)
        order.save()
        booklist = request.session.get("book")
        clotheList = request.session.get("clothes")
        electronicsList = request.session.get("electronics")
        for b in booklist:
            book = Book.objects.get(pk=b)
            book.inStock -= 1
            book.save()
            try:
                temp = bookorder.objects.get(book=book, order=order)
                temp.quantity += 1
                temp.save()
            except:
                temp = bookorder(book=book, order=order, quantity=1)
                temp.save()
        for c in clotheList:
            clothes = Clothe.objects.get(pk=c)
            clothes.inStock -= 1
            clothes.save()
            try:
                temp = clothesorder.objects.get(clothes=clothes, order=order)
                temp.quantity += 1
                temp.save()
            except:
                temp = clothesorder(clothes=clothes, order=order, quantity=1)
                temp.save()
        for e in electronicsList:
            electronics = Electronic.objects.get(pk=e)
            electronics.inStock -= 1
            electronics.save()
            try:
                temp = electronicsorder.objects.get(electronics=electronics, order=order)
                temp.quantity += 1
                temp.save()
            except:
                temp = electronicsorder(electronics=electronics, order=order, quantity=1)
                temp.save()
        request.session["book"] = []
        request.session["clothes"] = []
        request.session["electronics"] = []
        request.session["count"] = 0
        request.session["total"] = 0
        return redirect("/bookstore/index")
    return render(request, 'bookstore/index.html')
