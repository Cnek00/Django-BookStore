from django.shortcuts import render, get_object_or_404, redirect
from .models import Book , Category
from .forms import BookSearchForm

def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()  # ✅ Kategorileri ekledik
    form = BookSearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data.get('query', '')
        category = form.cleaned_data.get('category', None)

        if query:
            books = books.filter(title__icontains=query)
        
        if category:
            books = books.filter(categories=category)

    return render(request, 'books/book_list.html', {'books': books, 'categories': categories, 'form': form})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

from django.contrib.auth.decorators import login_required

from .models import Favorite

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Favorite

@login_required
def add_to_favorites(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, book=book)
    return redirect('favorite_list')

@login_required
def remove_from_favorites(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    Favorite.objects.filter(user=request.user, book=book).delete()
    return redirect('favorite_list')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Favorite

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'books/favorite_list.html', {'favorites': favorites})
