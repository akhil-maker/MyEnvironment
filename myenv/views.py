from django.db.models.query import QuerySet
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()
    x = []
    query = request.GET
    search = query.getlist('searchterm')
    if(len(search)!=0 and search[0]!=''):
        for i in posts:
            if(search[0] not in i.title):
                posts.filter(i)
    for i in range(0, len(posts), 2):
        l = []
        l.append(posts[i])
        if i+1 < len(posts):
            l.append(posts[i+1])
        x.append(l)
    context = {'posts':x}
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')