from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    searchterm = request.POST.get("searchterm")
    posts = Post.objects.all()
    x = []
    if searchterm != None:
        l = []
        for i in posts:
            if str(searchterm) in i.title:
                if len(l)==2:
                    x.append(l)
                    l.clear()
                l.append(i)
        if len(l)>0:
            x.append(l)
        context = {'posts':x}
        return render(request, 'index.html', context)
    else:            
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