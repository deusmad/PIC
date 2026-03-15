from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from .models import Article


def archive(request):
    posts = Article.objects.order_by('-created_date')
    return render(request, 'archive.html', {"posts": posts})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = {
            "title": request.POST.get("title", "").strip(),
            "text": request.POST.get("text", "").strip(),
        }

        if not form["title"] or not form["text"]:
            form["errors"] = "Не все поля заполнены"
            return render(request, "create_post.html", {"form": form})

        if Article.objects.filter(title=form["title"]).exists():
            form["errors"] = "Статья с таким названием уже существует"
            return render(request, "create_post.html", {"form": form})

        article = Article.objects.create(
            title=form["title"],
            text=form["text"],
            author=request.user
        )

        return redirect("get_article", article_id=article.id)

    return render(request, "create_post.html", {})


def user_login(request):
    if request.method == "POST":
        form = {
            "username": request.POST.get("username", "").strip(),
            "password": request.POST.get("password", "")
        }

        user = authenticate(
            request,
            username=form["username"],
            password=form["password"]
        )

        if user is None:
            form["errors"] = "Неверный логин или пароль"
            return render(request, "login.html", {"form": form})

        login(request, user)
        return redirect("archive")

    return render(request, "login.html", {})


def user_logout(request):
    logout(request)
    return redirect("archive")