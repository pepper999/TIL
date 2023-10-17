from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/delete', views.delete, name='delete'),
    path('<int:article_pk>/likes', views.likes, name='likes'),
]
