from django.shortcuts import render
from add_books import addbooks
# Create your views here.
def add_books(request):
    if request.method == 'POST':
        b_name = request.POST['bookName']
        b_author = request.POST['author']
        genre = request.POST['subject']
        addbooks(b_name,b_author,genre)
    render (request, 'add_books.html', {})
