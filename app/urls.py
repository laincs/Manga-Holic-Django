from django.urls import path
from .views import home, news, news_detail

app_name = 'app'

urlpatterns = [
    path('home/', home, name="home"),
    path('news/', news, name='news'),
    path('news_detail/<int:pk>/', news_detail, name='news_detail')
]
