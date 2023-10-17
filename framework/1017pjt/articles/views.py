from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def main(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles':articles
    }
    return render(request, 'articles/main.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('main')
    form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('main')


def likes(request, article_pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            article = Article.objects.get(pk=article_pk)
            if request.user in article.like_users.all():
                article.like_users.remove(request.user)
            else:
                article.like_users.add(request.user)
        return redirect('main')
    return redirect('accounts:login')