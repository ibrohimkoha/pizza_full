"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from pages import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    #pages urls 
    path('', views.home, name='home'),
    path('2/', views.home2, name='home2'),
    path('menu/', views.menu, name='menu'),
    path('menu2/', views.menu2, name='menu2'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog_right/', views.blog_right, name='blog_right'),
    path('blog_left/', views.blog_left, name='blog_left'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('products/',views.product_single, name='product_single'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('about_us/', views.about_us, name='about_us'),
]

