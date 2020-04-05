"""CRM_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.signin, name="login"),
    path('logout/', views.signout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('products/', views.products, name="products"),
    path('customer/<str:customer_id>/', views.customer, name="customer"),
    path('create_order/<str:customer_id>', views.createOrder, name="create_order"),
    path('update_order/<str:id>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:id>/', views.deleteOrder, name="delete_order"),
    path('delete_customer/<str:id>/', views.deleteCustomer, name="delete_customer")
]
