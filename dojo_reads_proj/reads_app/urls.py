from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_index),
    path('add', views.add_book),
    path('create', views.create_book),
    path('<int:book_id>', views.book_view),
    path('<int:book_id>/review/new', views.add_review),
    path('<int:book_id>/review/<int:review_id>/delete', views.delete_review),
]