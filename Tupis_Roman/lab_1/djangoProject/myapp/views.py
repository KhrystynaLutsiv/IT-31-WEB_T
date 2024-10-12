from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Відображення home.html

def about(request):
    return render(request, 'about.html')  # Відображення about.html (сторінка гри)
