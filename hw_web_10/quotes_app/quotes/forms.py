from django.forms import ModelForm, CharField, TextInput
from .models import Quote, Author


class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput())
    author = CharField(required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['quote', 'author']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=100, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=150, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']