from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/create/', views.create, name='create'),
    path('snake/<int:id>/', views.snake, name='snake'),  # Додаємо параметр id
    path('tictactoe/', views.tictactoe, name='tictactoe'),
    path('guessnumber/', views.guessnumber, name='guessnumber'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
