from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from .models import Author, Quote
from .forms import AuthorForm, QuoteForm



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
    quotes_list = Quote.objects.all()
    paginator = Paginator(quotes_list, 10) # 10 цитат на сторінку

    page = request.GET.get('page')
    try:
        quotes = paginator.page(page)
    except PageNotAnInteger:
        # Якщо сторінка не є цілим числом, відображаємо першу сторінку
        quotes = paginator.page(1)
    except EmptyPage:
        # Якщо сторінка виходить за межі діапазону, відображаємо останню сторінку результатів
        quotes = paginator.page(paginator.num_pages)

    return render(request, 'quotesapp/quotes_list.html', {'quotes': quotes})


@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/authors')
    else:
        form = AuthorForm()
    return render(request, 'quotesapp/add_author.html', {'form': form})


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/quotes")
    else:
        form = QuoteForm()

    return render(request, 'quotesapp/add_quote.html', {'form': form})


@login_required
def delete_quote(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)

    # Перевірка, що користувач має права на видалення цитати
    # Можна додати додаткові умови, наприклад, перевірку, чи користувач є автором цитати

    if request.method == 'POST':
        quote.delete()
        return redirect('/quotes')

    return render(request, 'quotesapp/delete_quote_confirm.html', {'quote': quote})
