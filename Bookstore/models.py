from django.db import models


# Create your models here.

class Fullname(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Address(models.Model):
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class Customer(models.Model):
    username = models.CharField(max_length=50, null=True, unique=True)
    password = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=20)
    dob = models.DateField(max_length=50)
    phone = models.CharField(max_length=15)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Shipment(models.Model):
    shipper = models.TextField()
    destination = models.TextField()
    fee = models.FloatField()


class Order(models.Model):
    orderName = models.TextField()
    orderEmail = models.TextField()
    quantity = models.IntegerField()
    total = models.FloatField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.TextField()
    type = models.TextField()
    price = models.BigIntegerField()
    inStock = models.IntegerField()
    discount = models.IntegerField()
    image = models.TextField()

class bookorder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Clothe(models.Model):
    name = models.TextField()
    type = models.TextField()
    price = models.BigIntegerField()
    inStock = models.IntegerField()
    discount = models.IntegerField()
    image = models.TextField()


class clothesorder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    clothes = models.ForeignKey(Clothe, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Electronic(models.Model):
    name = models.TextField()
    type = models.TextField()
    price = models.BigIntegerField()
    inStock = models.IntegerField()
    discount = models.IntegerField()
    image = models.TextField()


class electronicsorder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    electronics = models.ForeignKey(Electronic, on_delete=models.CASCADE)
    quantity = models.IntegerField()


def productFactory(productType):
    if productType == "book":
        return Book
    elif productType == "clothe":
        return Clothe
    elif productType == "electronic":
        return Electronic
    else:
        return
