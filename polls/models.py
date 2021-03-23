from django.db import models


# Create your models here.

class Fullname(models.Model):
    firstname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Address(models.Model):
    no = models.IntegerField()
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class Customer(models.Model):
    username = models.CharField(max_length=50,null=True,unique=True)
    password = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=20)
    dob = models.DateTimeField(max_length=50)
    phone = models.CharField(max_length=15)
    fullname = models.ForeignKey(Fullname, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

# class Question (models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('data published')
#
#     def __str__(self):
#         return self.question_text
#
# class Choice (models.Model):
#     question = models.ForeignKey(Question,on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

# def __str__(self):
#     return self.choice_text
