from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def home2(request):
    return render(request, 'home2.html')

def menu(request):
    return render(request, 'menu.html')

def menu2(request):
    return render(request, 'menu2.html')

def about_us(request):
    return render(request, 'about_us.html')

def blog(request):
    return render(request, 'blog.html')

def blog_left(request):
    return render(request, 'blog_left.html')

def blog_right(request):
    return render(request, 'blog_right.html')

def blog_single(request):
    return render(request, 'blog_single.html')

def contact(request):
    return render(request, 'contact.html')

def shopping_cart(request):
    return render(request, 'shopping_cart.html')

def product_single(request):
    return render(request, 'product_single.html')