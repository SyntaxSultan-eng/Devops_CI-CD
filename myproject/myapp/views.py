from django.shortcuts import render
from django.http import HttpResponse
from .models import Counter
  
def index(request):

    Counter.objects.create()
    
    total_count = Counter.objects.count()
    
    result = f"<h1>Счетчик записей в базе</h1>"
    result += f"<p>Всего записей в таблице: <strong>{total_count}</strong></p>"
    result += "<p>Обновите страницу чтобы добавить +1 запись</p>"

    return HttpResponse(result)

def check_db(request):
    from django.db import connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return HttpResponse("База данных подключена успешно!")
    except Exception as e:
        return HttpResponse(f"Ошибка подключения: {e}")
