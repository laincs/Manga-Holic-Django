from django.contrib.auth import authenticate, login as auth_login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import News

def home_view(request):
    latest_news = News.objects.all()[:5] 

    print("Latest News:", latest_news)

    context = {
        'latest_news': latest_news,
    }

    return render(request, 'app/home.html', context)

def ourClients_view(request):
    context = {
    }

    return render(request, 'app/ourClients.html', context)

def try_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('app:home')
        else:
            return render(request, 'app/login.html')

def login_view(request):
    return render(request, 'app/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('app:home')
        else:
            print(form.errors)  # Muestra los errores en la consola
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'app/signup.html', context)

def about_view(request):
    context = {
    }

    return render(request, 'app/about.html', context)

def news_view(request):
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

def news_detail_view(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'app/news_detail.html', {'news_item': news_item})
