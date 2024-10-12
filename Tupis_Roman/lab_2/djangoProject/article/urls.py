from django.urls import path
from .views import index, create, delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('delete/<int:article_id>/', delete, name='delete'),
]
