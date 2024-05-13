from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>', views.main, name='root_paginate'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('about_author/<str:fullname>', views.aboutauthor, name='about_author'),
]
