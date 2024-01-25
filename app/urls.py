from django.urls import path, re_path
from .views import home, news, news_detail, ourClients
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import serve

app_name = 'app'

urlpatterns = [
    path('home/', home, name="home"),
    path('clients/', ourClients, name="clients"),
    path('news/', news, name='news'),
    path('news_detail/<int:pk>/', news_detail, name='news_detail'),

    re_path(r'^(?!static/|media/|news_images).*$', RedirectView.as_view(url='/home/'))

]