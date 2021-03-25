from django.shortcuts import render, redirect
from Bookstore.form import *
from Bookstore.models import *
import win32api
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                Customer.objects.get(username=username,password=password);
                win32api.MessageBox(0, 'Đăng nhập thành công', 'Thông báo')
            except Customer.DoesNotExist:
                win32api.MessageBox(0, 'Sai tên đăng nhập hoặc mật khẩu ', 'Thông báo')
    else:
        form = LoginForm()
    return render(request, 'bookstore/Login.html', {'form':form})
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            # Save Fullname
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            fn = Fullname(firstname=first_name, middlename=middle_name, lastname=last_name)
            fn.save()

            # Save Address
            no = form.cleaned_data.get('number')
            street = form.cleaned_data.get('street')
            district = form.cleaned_data.get('district')
            city = form.cleaned_data.get('city')

            addr = Address(no=no, street=street, district=district, city=city)
            addr.save()

            # Save Customer
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            gender = form.cleaned_data.get('gender')
            dob = form.cleaned_data.get('dob')
            phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            customer = Customer(gender=gender, dob=dob, phone=phone, fullname=fn, address=addr, username=username,password=password)
            Customer.save(customer)
            response = redirect('/bookstore/login')
            return response
    else:
        form = SignInForm()
    return render(request, 'bookstore/signin.html', {'form': form})