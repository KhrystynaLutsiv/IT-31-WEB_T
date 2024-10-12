from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})

def create(request):
    if request.method == 'POST':
        article = Article.objects.create(
            title=request.POST['title'],
            description=request.POST['description']
        )
        return redirect('index')  # Повертаємось на головну сторінку
    return render(request, 'create.html')

def delete(request, article_id):
    article = Article.objects.get(id=article_id)
    article.delete()
    return redirect('index')

def index(request):
    articles = Article.objects.all()  # Отримуємо всі статті
    return render(request, 'index.html', {'articles': articles})  # Повертаємо шаблон
