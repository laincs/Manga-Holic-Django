from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import News

def home(request):
    latest_news = News.objects.all()[:5] 

    print("Latest News:", latest_news)

    context = {
        'latest_news': latest_news,
    }

    return render(request, 'app/home.html', context)

def ourClients(request):
    context = {
    }

    return render(request, 'app/ourClients.html', context)

def news(request):
    all_news = News.objects.all()

    paginator = Paginator(all_news, 8)
    page = request.GET.get('page')

    try:
        latest_news = paginator.page(page)
    except PageNotAnInteger:
        latest_news = paginator.page(1)
    except EmptyPage:
        latest_news = paginator.page(paginator.num_pages)

    context = {
        'latest_news': latest_news,
    }

    return render(request, 'app/news.html', context)

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'app/news_detail.html', {'news_item': news_item})