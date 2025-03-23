from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('books/', views.BookListView.as_view(), name='books'),  # List all books (CBV)
    path('authors/', views.AuthorListView.as_view(), name='authors'),  # List all authors (CBV)
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Book detail view (CBV)
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),  # Author detail view (CBV)
    
]
