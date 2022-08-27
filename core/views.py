from django.shortcuts import render

from blog.models import Post

def frontpage(request):
    post = Post.objects.all()
    return render(request, 'core/frontpage.html', { 'posts': post})

def about(request):
    return render(request, 'core/about.html')

