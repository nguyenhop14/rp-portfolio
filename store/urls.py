from django.urls import path

from .views import (
    create_book_normal,
    create_book_model_form,
    create_book_with_authors,
    BookListView,
)

app_name = 'store'

urlpatterns = [

    path('book/create_normal', create_book_normal, name='create_book_normal'),
    path('book/create_model', create_book_model_form, name='create_book_model_form'),
    path('book/create_with_author', create_book_with_authors, name='create_book_with_authors'),
    path('book/list', BookListView.as_view(), name='book_list'),

]