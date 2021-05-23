from django.urls import path
from . import views

app_name = 'Bookstore'
urlpatterns = [

    path('register', views.register, name='register'),

    path('login', views.login, name='login'),

    path('index', views.index, name="index"),

    path('book', views.getbook, name="getbook"),

    path('electronics', views.getElectronics, name="getElectronics" ),

    path('clothes', views.getClothes, name="getClothes" ),

    path('addcart/<str:type>/<int:id>', views.addcart),

    path('addtocart/<str:type>/<int:id>', views.addtocart)


    # path('index/electronic', views.electronic_view, name = "electronic"),

    # path('index/book', views.book_view, name="book"),

    # path('index/clothe', views.clothe_View, name="clothe")

]
