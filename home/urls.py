from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home.index.html'),
    path('about', views.about, name='home.about.html'),
]