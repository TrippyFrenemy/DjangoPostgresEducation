import json
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin
from .models import *


class AddDataAdmin(admin.ModelAdmin):
    actions = ['import_data']

    def import_data(self, request, queryset=None):
        import_data_from_json()
        self.message_user(request, "Data imported successfully")

    import_data.short_description = "Import data from JSON files"

    import_data.allow_empty = True


def import_data_from_json():
    # Імпорт авторів
    with open('scrappyquotes/authors.json', 'r', encoding='utf-8') as file:
        authors_data = json.load(file)
        for author_data in authors_data:
            Author.objects.get_or_create(
                fullname=author_data['fullname'],
                defaults={
                    'born_date': author_data['born_date'],
                    'born_location': author_data['born_location'],
                    'description': author_data['description']
                }
            )

    # Імпорт цитат
    with open('scrappyquotes/quotes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            try:
                author = Author.objects.get(fullname=quote_data['author'])
                Quote.objects.get_or_create(
                    author=author,
                    quote=quote_data['quote'],
                    defaults={'tags': quote_data['tags']}
                )
            except ObjectDoesNotExist:
                print(f"Author not found: {quote_data['author']}")



# Register your models here.
admin.site.register(Quote)
admin.site.register(Author, AddDataAdmin)
