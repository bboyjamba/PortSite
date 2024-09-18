from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('live', views.live, name='live'),
    path('portfolio', views.live, name='portfolio'),
    path('gallery', views.live, name='gallery'),
]