from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .models import Book, BookCategory
from .forms import BookForm

# Create your views here.


def main(request):
    books = Book.objects.filter(status='Published')
    form = BookForm()
    draft_books = Book.objects.filter(status='Draft')
    categories = BookCategory.objects.all()
    is_superuser = request.user.is_superuser


    category_id = request.GET.get('category')
    if category_id:
        books = books.filter(category_id=category_id)
    
    if not books.exists():
        no_books_message = 'Книг в выбранной категории не нашлось.'
    else:
        no_books_message = ''

    context ={
              'books':books,
              'no_books_message':no_books_message,
              'form':form,
              'draft_books':draft_books,
              'categories':categories,
              'is_superuser':is_superuser,
              }
    
    return render(request, 'main.html', context)

def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            review = form.cleaned_data['review']
            rate = form.cleaned_data['rate']
            status = form.cleaned_data['status']

            Book.objects.create(title=title,author=author,category=category,description=description,review=review,rate=rate,status=status)
            return redirect('main')
    else:
        form = BookForm()
    return redirect('main')

    #Так и не понял как все таки вывод ошибок в форму сделать ...
    #return render(request, 'main.html', {'form': form})

def book_detail(request, book_id):
    book = get_object_or_404(Book,id = book_id)
    is_superuser = request.user.is_superuser

    context = {
               'book':book,
               'is_superuser':is_superuser
               }
    return render(request,'detail.html',context)

def book_publish(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    book.status = Book.PUBLISHED
    book.save()
    return redirect('book_detail',book_id)

def book_unpublish(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    book.status = Book.DRAFT
    book.save()
    return redirect('book_detail',book_id)
