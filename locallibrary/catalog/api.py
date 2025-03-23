from ninja import NinjaAPI
from ninja.orm import create_schema
from typing import List, Optional
from .models import Author, Genre, Language, Book, BookInstance
from django.shortcuts import get_object_or_404
from ninja import Schema

api = NinjaAPI()

# AUTHOR SCHEMA
class AuthorSchema(Schema):
    first_name: str
    last_name: str
    date_of_birth: Optional[str] = None
    date_of_death: Optional[str] = None

# GENRE SCHEMA
class GenreSchema(Schema):
    name: str

# LANGUAGE SCHEMA
class LanguageSchema(Schema):
    name: str

# BOOK SCHEMA
class BookSchema(Schema):
    title: str
    author_id: int
    summary: str
    isbn: str
    language: str

# BOOKINSTANCE SCHEMA
class BookInstanceSchema(Schema):
    book_id: int
    imprint: str
    due_back: Optional[str] = None
    status: str

# AUTHOR ENDPOINTS
@api.get("/authors", response=List[AuthorSchema])
def list_authors(request):
    authors = Author.objects.all()
    return authors

@api.post("/authors", response=AuthorSchema)
def create_author(request, data: AuthorSchema):
    author = Author.objects.create(**data.dict())
    return author

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@api.put("/authors/{author_id}", response=AuthorSchema)
def update_author(request, author_id: int, data: AuthorSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in data.dict().items():
        setattr(author, attr, value)
    author.save()
    return author

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}

# GENRE ENDPOINTS
@api.get("/genres", response=List[GenreSchema])
def list_genres(request):
    genres = Genre.objects.all()
    return genres

@api.post("/genres", response=GenreSchema)
def create_genre(request, data: GenreSchema):
    genre = Genre.objects.create(**data.dict())
    return genre

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.put("/genres/{genre_id}", response=GenreSchema)
def update_genre(request, genre_id: int, data: GenreSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.name = data.name
    genre.save()
    return genre

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}

# LANGUAGE ENDPOINTS
@api.get("/languages", response=List[LanguageSchema])
def list_languages(request):
    languages = Language.objects.all()
    return languages

@api.post("/languages", response=LanguageSchema)
def create_language(request, data: LanguageSchema):
    language = Language.objects.create(**data.dict())
    return language

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.put("/languages/{language_id}", response=LanguageSchema)
def update_language(request, language_id: int, data: LanguageSchema):
    language = get_object_or_404(Language, id=language_id)
    language.name = data.name
    language.save()
    return language

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}

# BOOK ENDPOINTS
@api.get("/books", response=List[BookSchema])
def list_books(request):
    books = Book.objects.all()
    return books

@api.post("/books", response=BookSchema)
def create_book(request, data: BookSchema):
    book = Book.objects.create(**data.dict())
    return book

@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book

@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, data: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in data.dict().items():
        setattr(book, attr, value)
    book.save()
    return book

@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}

# BOOKINSTANCE ENDPOINTS
@api.get("/bookinstances", response=List[BookInstanceSchema])
def list_bookinstances(request):
    instances = BookInstance.objects.all()
    return instances

@api.post("/bookinstances", response=BookInstanceSchema)
def create_bookinstance(request, data: BookInstanceSchema):
    instance = BookInstance.objects.create(**data.dict())
    return instance

@api.get("/bookinstances/{instance_id}", response=BookInstanceSchema)
def get_bookinstance(request, instance_id: int):
    instance = get_object_or_404(BookInstance, id=instance_id)
    return instance

@api.put("/bookinstances/{instance_id}", response=BookInstanceSchema)
def update_bookinstance(request, instance_id: int, data: BookInstanceSchema):
    instance = get_object_or_404(BookInstance, id=instance_id)
    for attr, value in data.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return instance

@api.delete("/bookinstances/{instance_id}")
def delete_bookinstance(request, instance_id: int):
    instance = get_object_or_404(BookInstance, id=instance_id)
    instance.delete()
    return {"success": True}
from ninja import NinjaAPI
from ninja.orm import create_schema
from typing import List, Optional
from .models import Author, Genre, Language, Book, BookInstance
from django.shortcuts import get_object_or_404
from ninja import Schema

api = NinjaAPI()

# AUTHOR SCHEMA
class AuthorSchema(Schema):
    first_name: str
    last_name: str
    date_of_birth: Optional[str] = None
    date_of_death: Optional[str] = None

# GENRE SCHEMA
class GenreSchema(Schema):
    name: str

# LANGUAGE SCHEMA
class LanguageSchema(Schema):
    name: str

# BOOK SCHEMA
class BookSchema(Schema):
    title: str
    author_id: int
    summary: str
    isbn: str
    language: str

# BOOKINSTANCE SCHEMA
class BookInstanceSchema(Schema):
    book_id: int
    imprint: str
    due_back: Optional[str] = None
    status: str

# AUTHOR ENDPOINTS
@api.get("/authors", response=List[AuthorSchema])
def list_authors(request):
    authors = Author.objects.all()
    return authors

@api.post("/authors", response=AuthorSchema)
def create_author(request, data: AuthorSchema):
    author = Author.objects.create(**data.dict())
    return author

@api.get("/authors/{author_id}", response=AuthorSchema)
def get_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    return author

@api.put("/authors/{author_id}", response=AuthorSchema)
def update_author(request, author_id: int, data: AuthorSchema):
    author = get_object_or_404(Author, id=author_id)
    for attr, value in data.dict().items():
        setattr(author, attr, value)
    author.save()
    return author

@api.delete("/authors/{author_id}")
def delete_author(request, author_id: int):
    author = get_object_or_404(Author, id=author_id)
    author.delete()
    return {"success": True}

# GENRE ENDPOINTS
@api.get("/genres", response=List[GenreSchema])
def list_genres(request):
    genres = Genre.objects.all()
    return genres

@api.post("/genres", response=GenreSchema)
def create_genre(request, data: GenreSchema):
    genre = Genre.objects.create(**data.dict())
    return genre

@api.get("/genres/{genre_id}", response=GenreSchema)
def get_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    return genre

@api.put("/genres/{genre_id}", response=GenreSchema)
def update_genre(request, genre_id: int, data: GenreSchema):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.name = data.name
    genre.save()
    return genre

@api.delete("/genres/{genre_id}")
def delete_genre(request, genre_id: int):
    genre = get_object_or_404(Genre, id=genre_id)
    genre.delete()
    return {"success": True}

# LANGUAGE ENDPOINTS
@api.get("/languages", response=List[LanguageSchema])
def list_languages(request):
    languages = Language.objects.all()
    return languages

@api.post("/languages", response=LanguageSchema)
def create_language(request, data: LanguageSchema):
    language = Language.objects.create(**data.dict())
    return language

@api.get("/languages/{language_id}", response=LanguageSchema)
def get_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    return language

@api.put("/languages/{language_id}", response=LanguageSchema)
def update_language(request, language_id: int, data: LanguageSchema):
    language = get_object_or_404(Language, id=language_id)
    language.name = data.name
    language.save()
    return language

@api.delete("/languages/{language_id}")
def delete_language(request, language_id: int):
    language = get_object_or_404(Language, id=language_id)
    language.delete()
    return {"success": True}

# BOOK ENDPOINTS
@api.get("/books", response=List[BookSchema])
def list_books(request):
    books = Book.objects.all()
    return books

@api.post("/books", response=BookSchema)
def create_book(request, data: BookSchema):
    book = Book.objects.create(**data.dict())
    return book

@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book

@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, data: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in data.dict().items():
        setattr(book, attr, value)
    book.save()
    return book

@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"success": True}

# BOOKINSTANCE ENDPOINTS
@api.get("/bookinstances", response=List[BookInstanceSchema])
def list_bookinstances(request):
    instances = BookInstance.objects.all()
    return instances

@api.post("/bookinstances", response=BookInstanceSchema)
def create_bookinstance(request, data: BookInstanceSchema):
    instance = BookInstance.objects.create(**data.dict())
    return instance

@api.get("/bookinstances/{instance_id}", response=BookInstanceSchema)
def get_bookinstance(request, instance_id: int):
    instance = get_object_or_404(BookInstance, id=instance_id)
    return instance

@api.put("/bookinstances/{instance_id}", response=BookInstanceSchema)
def update_bookinstance(request, instance_id: int, data: BookInstanceSchema):
    instance = get_object_or_404(BookInstance, id=instance_id)
    for attr, value in data.dict().items():
        setattr(instance, attr, value)
    instance.save()
    return instance

@api.delete("/bookinstances/{instance_id}")
def delete_bookinstance(request, instance_id: int):
    instance = get_object_or_404(BookInstance, id=instance_id)
    instance.delete()
    return {"success": True}
