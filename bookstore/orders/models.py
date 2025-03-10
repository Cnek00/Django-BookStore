from django.db import models
from users.models import CustomUser
from books.models import Book

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Kullanıcı")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Sipariş Tarihi")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Toplam Fiyat")
    is_paid = models.BooleanField(default=False, verbose_name="Ödeme Yapıldı mı?")

    def __str__(self):
        return f"{self.user.username} - Sipariş ID: {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="Sipariş")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Kitap")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Adet")

    def __str__(self):
        return f"{self.quantity} x {self.book.title} ({self.order.user.username})"
