from django.shortcuts import render

def home(request):
    return render(request, 'games/home.html')

def create(request):
    return render(request, 'games/create.html')

def snake(request, id):
    return render(request, 'games/snake.html', {'id': id})

def tictactoe(request):
    return render(request, 'games/tictactoe.html')

def guessnumber(request):
    return render(request, 'games/guessnumber.html')

def about(request):
    return render(request, 'games/about.html')

def contact(request):
    return render(request, 'games/contact.html')
