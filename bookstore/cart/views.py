from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from books.models import Book
from cart.models import Cart, CartItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    # Toplam fiyat hesaplama
    total_price = sum(item.book.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price  # Template'e toplam fiyatı gönderiyoruz
    })


@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Kitabı getir
    cart, created = Cart.objects.get_or_create(user=request.user)  # Kullanıcının sepetini al veya oluştur
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)  # Kitabı sepete ekle

    if not item_created:
        # Kullanıcının eklemek istediği miktar stoktan fazla mı kontrol et
        if cart_item.quantity < book.stock:
            cart_item.quantity += 1
            cart_item.save()
        else:
            messages.error(request, "Stok miktarından fazla ürün ekleyemezsiniz!")
    else:
        # Yeni ekleniyorsa ve stokta varsa ekle
        if book.stock > 0:
            cart_item.quantity = 1
            cart_item.save()
        else:
            messages.error(request, "Bu ürün stokta yok!")

    return redirect('view_cart')


@login_required
def remove_from_cart(request, book_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.filter(cart=cart, book_id=book_id).first()

    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('view_cart')
