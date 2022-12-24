from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product, Pages, Articles
from authentication.forms import LoginForm
from django.contrib.auth import authenticate, login

from cart.forms import CartAddProductForm

# Главная 
def homePage(request):
    articles = Articles.objects.filter(id=1)
    context = {
        'article': articles
    }
    return render(request, 'main/index.html', context)   


# Sale
def salePage(request):
    articles = Articles.objects.filter(id=3)
    articles2 = Articles.objects.filter(id=5)
    articles3 = Articles.objects.filter(id=6)
    articles4 = Articles.objects.filter(id=7)
    context = {
        'article': articles,
        'article2': articles2,
        'article3': articles3,
        'article4': articles4,
    }
    
    return render(request, 'main/sale.html', context) 

  

# """ Отображение всех товаров """
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(id=2)
    # categories = Category.objects.all()
    # products = Product.objects.filter(category__id__exact=1) 
    products = Product.objects.filter(available=True) 
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if request.user.is_authenticated:
        return render(request,  'main/detail2.html',{'category': category, 'categories': categories, 'products': products })
    return redirect('main:login')


   
   

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'main/detail.html', {'product': product, 'cart_product_form': cart_product_form})


def clothes_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(pk__in=[1,2])
    products = []
    products.append( Product.objects.filter(category__id__exact=1))
    products.append(Product.objects.filter(category__id__exact=2))
    print(products)
    print(products)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/category/clothes.html', {'category': category, 'categories': categories, 'products': products })

def accessories_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(pk__in=[3,5])
    products = []
    products.append( Product.objects.filter(category__id__exact=3))
    products.append(Product.objects.filter(category__id__exact=5))
    print(products)
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/category/accessories.html', {'category': category, 'categories': categories, 'products': products })


def bags_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(id=4)
    products = []
    products.append( Product.objects.filter(category__id__exact=4))
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/category/bags.html', {'category': category, 'categories': categories, 'products': products })

def bijouterie_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(id=5)
    products = []
    products.append( Product.objects.filter(category__id__exact=5))
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/products/bijouterie.html', {'category': category, 'categories': categories, 'products': products })

def dresses_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(id=1)
    products = []
    products.append( Product.objects.filter(category__id__exact=1))
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/products/dresses.html', {'category': category, 'categories': categories, 'products': products })  

def glasses_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(id=3)
    products = []
    products.append( Product.objects.filter(category__id__exact=3))
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/products/glasses.html', {'category': category, 'categories': categories, 'products': products })

def jackets_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(id=2)
    products = []
    products.append( Product.objects.filter(category__id__exact=2))
    print(products)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'main/products/jackets.html', {'category': category, 'categories': categories, 'products': products })





def index(request):
    return render(request, 'main/index.html')

 

def informationPage(request):
    articles8 = Articles.objects.filter(id=8)
    articles9 = Articles.objects.filter(id=9)
    articles10 = Articles.objects.filter(id=10)
    context = {
        'article8': articles8,
        'article9': articles9,
        'article10': articles10,
    }
    return render(request, 'main/information.html', context)  


# страница входа корзина
def basketPage(request):
   
        if request.user.is_authenticated:
            return render(request, 'main/basket.html', {'user': request.user})
        else:
            return redirect(request,'main/login.html') 

    
       