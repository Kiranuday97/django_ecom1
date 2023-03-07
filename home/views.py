
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView,DeleteView
from .models import  Order, Products, Cart
from django.core.paginator import Paginator
from .forms import AddProductForm, CheckoutForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required






def home(request):
    
    pro = Products.objects.all()
    pgn = Paginator(pro,4)
    page_num = request.GET.get("page")
    page_obj = pgn.get_page(page_num)
    return render(request, 'home.html',{"prdct": page_obj}) 




@login_required
def AddItems(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.info(request, 'Product added successfully!')
            return redirect('home')  
    else:
        form = AddProductForm()
    return render(request, 'sell.html', {'form': form})


# def search(request):
#     item = request.GET['item']
#     pro = Products.objects.filter(name__icontains = item)

#     return render(request, "home.html", {"products": pro})



def search(request):
    item = request.GET.get('item')
    if item:
        pro = Products.objects.filter(title__icontains=item)
    else:
        pro = Products.objects.none()
    return render(request, "search.html", {"products": pro})

def productview(request, id):
    prds = Products.objects.get(id=id)
    return render(request, 'productview.html',{"products": prds})     


@login_required
def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, "Product added to cart.")
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id)
    cart_item.delete()
    messages.success(request, "Product removed from cart.")
    return redirect('cart')




@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum([item.product.price * item.quantity for item in cart_items])
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            try:
                order = Order.objects.create(user=request.user, total_price=total_price, )
                for item in cart_items:
                    order.products.add(item.product)
                order.save()
                messages.success(request, "Order placed successfully.")
                return redirect('order', order_id=order.id)
            except Exception as e:
                messages.error(request, f"Error placing order: {e}")
        else:
            messages.error(request, "Invalid form data.")
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price, 'products': cart_items})


@login_required
def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    products = order.products.all()
    return render(request, 'order.html', {'order': order, 'products': products})


@login_required
def update_cart(request, product_id):
    quantity = request.POST.get('quantity')

    try:
        cart_item = Cart.objects.get(user=request.user, product_id=product_id)
        cart_item.quantity = quantity
        cart_item.save()
    except Cart.DoesNotExist:
        cart_item = Cart.objects.create(
            user=request.user,
            product=Products.objects.get(id=product_id),
            quantity=quantity
        )

    messages.success(request, 'Your cart has been updated.')
    return redirect('cart')


def editproduct(request, id):
    global pro
    pro =Products.objects.get(id=id)
    form = AddProductForm(instance=pro)
    return render(request, 'editproduct.html',{"form":form})

def editproductsave(request):
    if request.method=="POST":
        
        form = AddProductForm(request.POST, request.FILES,instance=pro)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'home.html',{"form":form})




def deleteproduct(request, id):
    product=Products.objects.get(id=id)
    product.delete()
    return redirect('home')