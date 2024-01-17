from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = {
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
}