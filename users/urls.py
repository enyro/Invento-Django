from django.urls import path

from . import views

urlpatterns = [  
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('users',views.users,name='users'),
    path('reset-password',views.resetPassword,name='reset-password'),

    path('api/v1/signin', views.signinApi, name="sigin-api"),
    path('api/v1/users', views.getUsers, name="users-api"),
    path('api/v1/create-user', views.create, name='create-user-api'),
    path('api/v1/reset-password', views.resetPasswordApi, name='reset-password-api'),
    path('api/v1/edit-user',views.editUser,name='edit-user-api'),
    path('api/v1/admin-reset-password', views.resetPasswordAdminApi, name='reset-password=admin-api'),
]