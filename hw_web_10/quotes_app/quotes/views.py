from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .forms import QuoteForm, AuthorForm
from .models import Author
from .utils import get_mongodb


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_per_pege = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_per_pege})


def quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/quote.html', {'form': form})

    return render(request, 'quotes/quote.html', {'form': QuoteForm()})


def author(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/author.html', {'form': form})

    return render(request, 'quotes/author.html', {'form': AuthorForm()})


def description_auth(request, id_):
    authors = Author.objects.filter(pk=id_).all()
    return render(request, template_name='quotes/descript_author.html', context={'authors': authors})



