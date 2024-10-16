from django.urls import path
from .views import home , snake , tictactoe





urlpatterns = [
    path('', home, name='home'),
    path('snake', snake, name='snake'),
    path('tictactoe', tictactoe, name='tictactoe'),
 

]