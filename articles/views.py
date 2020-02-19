from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articles
from . import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
def articles_list(request):
    articles = Articles.objects.all().order_by('-date')
    args = {'articles': articles}
    return render(request, 'articles/articleList.html', args)

def articles_detail(request, slug):
    #return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)
    args = {'article': article}
    return render(request, 'articles/articleDetail.html', args)

@login_required(login_url="/accounts/login/")
def articles_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/articles/')
    else:
        form = forms.CreateArticle()
    args = {'form' : form}
    return render(request, 'articles/articleCreate.html', args)
