from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance
def index(request):
    """View function for the home page."""
    
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    # Retrieve the session visit count, defaulting to 0 if not set
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1  # Increment count
    request.session['num_visits'] = num_visits  # Store updated count in session

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,  # Pass visit count to template
    }

    return render(request, 'catalog/index.html', context)

class BookListView(generic.ListView):
    """Class-based view for listing all books."""
    model = Book
    paginate_by = 10  # Enables pagination

class BookDetailView(generic.DetailView):
    """Class-based view for displaying book details."""
    model = Book

class AuthorListView(generic.ListView):
    """Class-based view for listing all authors."""
    model = Author
    paginate_by = 10  # Enables pagination

class AuthorDetailView(generic.DetailView):
    """Class-based view for displaying author details."""
    model = Author
