from django.urls import path
from . import views  # Імпорт твого файлу з в'юшками

urlpatterns = [
    path('', views.home, name='home'),   # Головна сторінка
    path('about/', views.about, name='about'),  # Сторінка гри
]
