from django.urls import path

from . import views

urlpatterns = [ 
    path('create-user',views.create,name='create-user'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('users',views.users,name='users'),
]