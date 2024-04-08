from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CartItems, OrderItem
from core.models import Produks
from django.contrib.auth.decorators import login_required


@login_required
def Cart(request):
    carts = CartItems.objects.filter(create_by = request.user)
    jumlah = CartItems.objects.filter(create_by = request.user).count()
    total_harga = 0
    for cart in carts:
        cart.subtotal = cart.produk.price * cart.quantity
        total_harga += cart.produk.price * cart.quantity  
    return render(request, 'cart/index.html', {
        'carts':carts,
        'total_harga':total_harga,
        'jumlah':jumlah
    })

@login_required
def addcart(request):
    if request.method == 'POST':
        produk_id = request.POST.get('produk_id')
        quantity = request.POST.get('quantity')
        try:
            produk = Produks.objects.get(id = produk_id)
            #tambahkan produk dengan produk yang sama
            cart_item, created = CartItems.objects.get_or_create(produk = produk, create_by=request.user, defaults={'quantity': quantity})
            if not created:
                cart_item.quantity += int(quantity)
                cart_item.save()
            messages.success(request, f'Item {produk.name} berhasil ditambahkan ke keranjang.')
        except Produks.DoesNotExist:
            messages.error(request, 'Produk tidak ditemukan.')
        return redirect('/cart')
    else:
        return redirect('/cart')


@login_required
def orderproduk(request):
    if request.method == 'POST':
        produk_id = request.POST.get('produk_id')
        quantity = request.POST.get('quantity')
        try:
            produk = Produks.objects.get(id = produk_id)
            order_item, created = OrderItem.objects.get_or_create(username = request.user, produk=produk, defaults={'quantity': quantity})
            if not created:
                order_item.quantity += int(quantity)
                order_item.save()
            messages.success(request, f'Item {produk.name} berhasil order.')
        except Produks.DoesNotExist:
            messages.error(request, 'Produk tidak di temukan.')
        return redirect('/cart/getorder')
    else:
        return redirect('/cart/getorder')

@login_required
def cartorder(request):
    if request.method == 'POST':
        cart_id = request.POST.get('cart_id')
        quantity = request.POST.get('quantity')
   
        try:
            cart = CartItems.objects.get(id = cart_id)
          
            order_cart, created = OrderItem.objects.get_or_create(username = request.user, produk = cart.produk, defaults={'quantity':quantity})
            if not created:
                order_cart.quantity += int(quantity)
                order_cart.save()
            messages.success(request, f'itenm {cart.produk.name} berhasil di order')
            cart.delete()
        except CartItems.DoesNotExist:
            messages.error(request, 'cart item tidak di temukan')
        return redirect('/cart/getorder')
    else:
        return redirect('/cart/getorder')

@login_required
def allorder(request):
    if request.method == 'POST':
        carts = CartItems.objects.filter(create_by = request.user)

        for cart in carts:
            order_cart, created =   OrderItem.objects.get_or_create(username = request.user, produk = cart.produk, defaults={'quantity':cart.quantity})
            if not created:
                order_cart.quantity += int(cart.quantity) 
                order_cart.save()
            cart.delete()

        messages.success(request, 'Semua item di keranjang berhasil dipesan.')
        return redirect('/cart/getorder') 
    else:
        return redirect('/cart/getorder')       

     

@login_required
def getorderproduk(request):
    orders = OrderItem.objects.filter(username = request.user)
    total_order = 0
    for order in orders:
        total_order += order.produk.price * order.quantity


    return render(request, 'cart/order.html', {
        'orders':orders,
        'total_order':total_order  
    })


@login_required
def deletecart(request, pk):
    cart = get_object_or_404(CartItems, pk=pk)
    cart.delete()

    return redirect('/cart')