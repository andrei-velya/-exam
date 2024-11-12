from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('book_add',book_add,name='book_add'),
    path('books/<int:book_id>',book_detail, name='book_detail'),
    path('books/<int:book_id>/publish',book_publish, name='book_publish'),
    path('books/<int:book_id>/unpublish',book_unpublish, name='book_unpublish'),
]
