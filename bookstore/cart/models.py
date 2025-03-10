from django.db import models
from books.models import Book
from users.models import CustomUser

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Kullanıcı")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")

    def __str__(self):
        return f"{self.user.username} - Sepeti"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items", verbose_name="Sepet")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Kitap")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Adet")

    def __str__(self):
        return f"{self.quantity} x {self.book.title} ({self.cart.user.username})"
