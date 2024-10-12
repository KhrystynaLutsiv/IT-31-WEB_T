from django.urls import path
from . import views  # Імпорт твого файлу з в'юшками

urlpatterns = [
    path('', views.index, name='index'),   # Головна сторінка
    path('about/', views.about, name='about'),  # Сторінка гри
]
