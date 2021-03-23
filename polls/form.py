from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class SignInForm(UserCreationForm):
    username = forms.CharField(label=_('Tên tài khoản'),max_length=30, required=True,help_text='Tên tài khoản phải dài hơn 8 chữ hoặc chữ số')
    first_name = forms.CharField(label=_('Họ'),max_length=30, required=False)
    middle_name = forms.CharField(label=_('Tên đệm'),max_length=30, required=False)
    last_name = forms.CharField(label=_('Tên'),max_length=30, required=False)
    password1 = forms.CharField(label=_("Mật khẩu"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(label=_("Nhập lại mật khẩu"),widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),strip=False,help_text=_("Nhập lại mật khẩu đã nhập ở trên"),)
    number = forms.IntegerField(label=_('Số nhà'),required=False)
    street = forms.CharField(label=_('Đường'),max_length=30, required=False)
    district = forms.CharField(label=_('Quận'), max_length=30, required=False)
    city = forms.CharField(label=_('Thành phố'), max_length=30, required=False)
    gender = forms.CharField(label=_('Giới tính'),max_length=30,required=False)
    dob = forms.DateTimeField(label=_('Ngày sinh'),required=False)
    phone = forms.CharField(label=_('Số điện thoại'),required=False)

class LoginForm(forms.Form):
    username = forms.CharField(label=_('Tên tài khoản'),max_length=30, required=True)
    password = forms.CharField(label=_("Mật khẩu"), strip=False,widget=forms.PasswordInput())
