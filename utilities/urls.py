from django.urls import path

from . import views

urlpatterns = [  
    path('utilities',views.utilities,name='utilities'),

    path('api/v1/utilities',views.utilitiesData,name='utilities-api'),
    path('api/v1/create-utility',views.createUtility,name='create-utilitie-api'),
]