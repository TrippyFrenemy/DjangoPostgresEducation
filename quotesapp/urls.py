from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name="main"),
    path('authors/', views.authors_list, name='authors_list'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quotes/', views.quotes_list, name='quotes_list'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('quotes/delete/<int:quote_id>/', views.delete_quote, name='delete_quote'),
]
