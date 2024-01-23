from django.urls import path
from .views import home, news

urlpatterns = [
    path('home/', home, name="home"),
    path('news/', news, name='news'),
]
