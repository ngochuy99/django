from django.urls import path
from . import views

app_name = 'Bookstore'
urlpatterns = [

    path('signin',views.signin,name = 'signin'),

    path('login',views.login,name = 'login')
    #
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
