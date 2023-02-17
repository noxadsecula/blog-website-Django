from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from django.urls import reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "index.html",{"articles":articles,"keyword":keyword})
    articles = Article.objects.all()
    return render(request,"index.html",{"articles":articles})
    

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html",{"articles":articles,"keyword":keyword})
    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

def about(request):
    return render(request, "about.html")

@login_required(login_url="login")
def dashboard(request):
    articles = Article.objects.filter( author = request.user)
    context = {
        "articles": articles
    }
    return render(request, "dashboard.html",context)

@login_required(login_url="login")
def addArticles(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()
        
        messages.success(request,"Article successfully added.")
        return redirect("dashboard")
    
    
    
    
    
    content = {
        "form":form
    }
    return render(request,"addarticle.html",content)

@login_required(login_url="login")
def updateArticle(request,id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()
        
        messages.success(request,"Article successfully updated.")
        return redirect("dashboard")
    context = {
        "form":form
    }
    return render(request, "update.html",context)


@login_required(login_url="login")
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)

    article.delete()
    messages.success(request,"Article "+ str(id) + " deleted.")
    return redirect("dashboard")


def detailView(request,id):
    # article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()

    context = {
        "article":article,
        "comments":comments
    }

    return render(request, "detail.html",context)

def addComment(request,id):
    article = get_object_or_404(Article, id = id)

    if request.method == "POST":
        commentAuthor = request.POST.get("commentAuthor")
        commentContent = request.POST.get("commentContent")
        
        newComment = Comment(commentAuthor = commentAuthor, commentContent = commentContent)

        newComment.article = article
        newComment.save()

    return redirect(reverse("detail",kwargs={"id":id}))