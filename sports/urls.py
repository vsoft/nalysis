from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'sports'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    re_path('(?P<pk>[0-9]+)/', views.DetailsView.as_view(), name='detail'),
    path('nfl/', views.NFLView.as_view(), name='nfl'),
    path('nba/', views.NBAView.as_view(), name='nba'),
    path('about/', views.AboutView.as_view(), name='about'),
]