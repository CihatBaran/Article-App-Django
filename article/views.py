from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from article.forms import ArticleForm
from article.models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
# Article > views.py


def index(request):
    context = {"message": "this is message from DJANGO",
               "number": 20,
               "numbers": [1, 2, 3, 4, 5, 6]}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def detail(request, id):
    return HttpResponse(f"Detail: {int(id)}")


@login_required(login_url="user:login")
def dashboard(request):

    article = Article.objects.filter(author=request.user)

    context = {
        "articles": article,
        "counter": 1
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES or None)

        if form.is_valid():

            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Successfully Added")
            return redirect("article:dashboard")
        else:
            return render(request, "article.html")

    else:
        form = ArticleForm()
        context = {
            "forms": form
        }
        return render(request, "article.html", context)


@login_required(login_url="user:login")
def ind_article(request, id):
    if request.method == "POST":
        print("method is post")
        pass
    else:

        # indv_article = Article.objects.get(id=id)
        indv_article = get_object_or_404(Article, id=id)
        context = {
            "indv_article": indv_article
        }
        return render(request, "ind_article.html", context)


@login_required(login_url="user:login")
def ind_article_delete(request, id):
    article = get_object_or_404(Article, id=id)

    article.delete()

    messages.success(request, "Successfully deleted!")
    return redirect("article:dashboard")


@login_required(login_url="user:login")
def ind_article_edit(request, id):
    article = get_object_or_404(Article, id=id)

    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Article Updated")
        return redirect("article:dashboard")
    return render(request, "update.html", {"forms": form})

    return render(request, "update.html")
