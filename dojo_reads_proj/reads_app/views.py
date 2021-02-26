from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book, Author, Review
from login_app.models import User

def books_index(request):
    if not 'user_id' in request.session:
        messages.error(request, "You are not logged in.")
        return redirect("/")
    user_first_name = request.session['first_name']
    context = {
        "user_first_name": user_first_name,
        "reviews": Review.objects.order_by('-id')[:3],
        "books": Book.objects.all()
    }
    return render(request, "books_index.html", context)

# --------------- Book Creation ------------------------------

def add_book(request):
    context = {
        "authors": Author.objects.all()
    }

    print("add book page")
    return render(request, "add_book.html", context)

def create_book(request):
    user = User.objects.get(id = request.session['user_id'])

    # make book object
    new_book = Book.objects.create(
        title = request.POST['title']
    )

    # add the user to the instance of the book
    new_book.users.add(user)

    # determine if new or exsiting author and add
    if len(request.POST['add_new_author']) <= 0:
            new_book.authors.add(Author.objects.get(id = request.POST['author']))
    else:
        new_book.authors.add(create_author(request))

    # create the review
    review = Review.objects.create(
        rating = request.POST['rating'],
        comment = request.POST['review_comment'],
        created_by = User.objects.get(id = request.session['user_id']),
        book = Book.objects.get(id = new_book.id)
    )

    print("book creation")
    return redirect("/books")

# --------------- Author Creation ------------------------------

def create_author(request):
    new_author = Author.objects.create(
        name = request.POST['add_new_author']
    )
    return(new_author)

# --------------- Review Creation ------------------------------

def add_review(request, book_id):

    review = Review.objects.create(
        rating = request.POST['rating'],
        comment = request.POST['review_comment'],
        created_by = User.objects.get(id = request.session['user_id']),
        book = Book.objects.get(id = book_id)
    )
    return redirect(f"/books/{book_id}")

# --------------- Book View ------------------------------

def book_view(request, book_id):
    this_book = Book.objects.get(id=book_id)
    context = {
        "book": this_book
    }
    return render(request, "book_view.html", context)

# --------------- Delete Review ------------------------------

def delete_review(request, book_id, review_id):
    this_book = Book.objects.get(id=book_id)
    this_book.reviews.get(id=review_id).delete()
    return redirect(f"/books/{this_book.id}")

# --------------- User View ------------------------------

def user_dispaly(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        "user": 
    }
    return render(request, "user_page.html")
