from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('article/<aid>', views.article, name='article'),
    path('comment/<aid>', views.comment, name='comment'),
]
