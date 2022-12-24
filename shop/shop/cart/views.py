from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product, Orders
from .cart import Cart, Like
from .forms import CartAddProductForm, LikeAddProductForm, OrdersbuyForm




@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    
 
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
    
def orders_buy_Page(request):
    if request.method == "POST":
        form = OrdersbuyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'main/ordersbuy.html', locals()) 
    else:
        form = OrdersbuyForm()
    return render(request, 'main/ordersbuy.html', locals()) 



    # form = OrdersbuyForm(request.POST or None)
    # if request.method == "POST" and form.is_valid():
    #     print(request.POST)
    #     print(form.cleaned_data)
    # new_form = form.save()
    # return render(request, 'main/ordersbuy.html', locals()) 

def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'update': True})
    
    return render(request, 'main/detail2.html', {'cart': cart})




    
@require_POST
def like_add(request, product_id):
    like = Like(request)
    product = get_object_or_404(Product, id=product_id)
    form = LikeAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        like.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:like_detail')


def like_remove(request, product_id):
    like = Like(request)
    product = get_object_or_404(Product, id=product_id)
    like.remove(product)
    return redirect('cart:like_detail')


def like_detail(request):
    like = Like(request)
    for item in like:
        item['update_quantity_form'] = LikeAddProductForm(initial={'quantity': item['quantity'],'update': True})
    return render(request, 'main/like.html', {'cart': like})
