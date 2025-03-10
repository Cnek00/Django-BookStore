from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from .models import Order, OrderItem
from cart.views import view_cart
 
@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if request.method == "POST":
        order = Order.objects.create(user=request.user, total_price=0, is_paid=True)

        total_price = 0
        for item in cart_items:
            OrderItem.objects.create(order=order, book=item.book, quantity=item.quantity)
            total_price += item.book.price * item.quantity

        order.total_price = total_price
        order.save()

        cart_items.delete()

        return redirect('order_success', order.id)
    
    total_price = sum(item.book.price * item.quantity for item in cart_items)

    return render(request, 'orders/checkout.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price  # Template'e toplam fiyatı gönderiyoruz
    })



def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_success.html', {'order': order})

