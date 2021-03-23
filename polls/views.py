from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
import win32api
from django.views import generic
from polls.form import SignInForm,LoginForm
from .models import Customer, Address, Fullname


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

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
    return render(request,'polls/Login.html',{'form':form})
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            middle_name = form.cleaned_data.get('middle_name')
            last_name = form.cleaned_data.get('last_name')
            no = form.cleaned_data.get('number')
            street = form.cleaned_data.get('street')
            district = form.cleaned_data.get('district')
            city = form.cleaned_data.get('city')
            gender = form.cleaned_data.get('gender')
            dob = form.cleaned_data.get('dob')
            phone = form.cleaned_data.get('phone')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            print(password)
            #Save Fullname
            fn = Fullname(firstname=first_name,middlename=middle_name,lastname=last_name)
            fn.save()
            #Save Address
            addr = Address(no=no,street=street,district=district,city=city)
            addr.save()
            #Save Customer
            customer = Customer(gender=gender,dob=dob,phone=phone,fullname=fn,address=addr,username=username,password=password)
            customer.save()
    else:
        form = SignInForm()
    return render(request, 'polls/signin.html', {'form': form})


