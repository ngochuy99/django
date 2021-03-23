from django.contrib import admin
from .models import Customer,Fullname,Address
# Register your models here.

admin.site.register(Fullname)
admin.site.register(Address)
admin.site.register(Customer)