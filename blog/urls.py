from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='blog'),
    path('<int:blog_id>/', views.article, name='article'),
]
