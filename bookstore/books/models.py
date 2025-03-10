from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kitap Adı")
    author = models.CharField(max_length=255, verbose_name="Yazar")
    description = models.TextField(verbose_name="Açıklama", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=0, verbose_name="Stok Miktarı")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")
    categories = models.ManyToManyField(Category, related_name="books")


    def __str__(self):
        return self.title


from django.conf import settings
from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')  # Aynı kullanıcı aynı kitabı birden fazla kez favorilere ekleyemesin.
