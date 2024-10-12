from django.contrib import admin
from django.urls import path, include
from article.views import index  # Імпортуйте вашу view для домашньої сторінки

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('article.urls')),  # Підключення URL статей
    path('', index, name='home'),  # Додайте цей рядок для маршруту домашньої сторінки
]
