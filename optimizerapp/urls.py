from django.urls import path
from . import views

urlpatterns=[

    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('app_page',views.app_page,name='app_page'),
    path('logout',views.logout,name='logout'),
    path('Application',views.Application,name='Application'),
    path('register',views.register,name='register'),
   
    
]