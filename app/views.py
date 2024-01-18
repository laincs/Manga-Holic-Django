from django.shortcuts import render
from .models import News

def home(request):
    # Obtener las últimas noticias (ajusta según tu lógica)
    latest_news = News.objects.all()[:3]  # Obtener las últimas 3 noticias

    # Imprimir para verificar en la consola de desarrollo
    print("Latest News:", latest_news)

    # Pasar las noticias a la plantilla
    context = {
        'latest_news': latest_news,
    }

    return render(request, 'app/home.html', context)
