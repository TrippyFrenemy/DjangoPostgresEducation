from django.shortcuts import render, get_object_or_404

from .models import Author, Quote


# Create your views here.
def main(request):
    return render(request, 'quotesapp/index.html')


def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'quotesapp/authors_list.html', {'authors': authors})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotesapp/author_detail.html', {'author': author})


def quotes_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotesapp/quotes_list.html', {'quotes': quotes})
