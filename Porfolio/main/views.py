from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def projects(request):
    return render(request, 'main/projects.html')

def contact(request):
    if request.method == 'POST':
        # Обработка формы (сохранение в БД или отправка email)
        pass
    return render(request, 'main/contact.html')
