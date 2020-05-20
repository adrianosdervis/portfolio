from django.shortcuts import render, get_object_or_404
from .models import Blog


def home(request):
    blogs = Blog.objects.order_by('-date')
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context)


def article(request, blog_id):
    # article = Blog.objects.all().get(id=blog_id)
    article = get_object_or_404(Blog, pk=blog_id)
    context = {'article': article}
    return render(request, 'blog/article.html', context)
