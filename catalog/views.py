from django.shortcuts import render
import json

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        data = {'name': name, 'phone': phone, 'message': message}
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)


    return render(request, 'catalog/contacts.html')