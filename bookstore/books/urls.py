from django.urls import path
from .views import book_list, book_detail
from .views import add_to_favorites, remove_from_favorites, favorite_list


urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:book_id>/', book_detail, name='book_detail'),
    path('favorites/add/<int:book_id>/', add_to_favorites, name='add_to_favorites'),
    path('favorites/remove/<int:book_id>/', remove_from_favorites, name='remove_from_favorites'),
    path('favorites/', favorite_list, name='favorite_list'),]
