from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Article


def archive(request):
    template_name = 'archive.html'
    return render(request, template_name, {"posts": Article.objects.all()})


def get_article(request, pk):
    post = get_object_or_404(
        Article,
        pk=pk
    )
    template_name = 'article.html'
    context = {"post": post}
    return render(request, template_name, context)


def create_post(request):
    if not request.user.is_authenticated:
        raise Http404

    if request.method == "POST":
        form = {
            'text': request.POST.get("text", ""),
            'title': request.POST.get("title", "")
        }

        if not form["text"] or not form["title"]:
            form['errors'] = "Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})

        if Article.objects.filter(title=form['title']).exists():
            form['errors'] = "Статья с таким названием уже существует. Придумайте другое."
            return render(request, 'create_post.html', {'form': form})

        article = Article.objects.create(
            text=form["text"],
            title=form["title"],
            author=request.user
        )

        return redirect('get_article', article_id=article.id)

    return render(request, 'create_post.html', {})


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
    template_name = 'archive'
    return redirect(template_name)


def user_registration(request):
    template_name = 'register.html'
    if request.method == "POST":
        form = {
            "username": request.POST.get("username", "").strip(),
            "password": request.POST.get("password", ""),
            "password2": request.POST.get("password2", "")
        }

        if not form["username"] or not form["password"] or not form["password2"]:
            form["errors"] = "Не все поля заполнены"
            return render(request, "register.html", {"form": form})

        if form["password"] != form["password2"]:
            form["errors"] = "Пароли не совпадают"
            return render(request, "register.html", {"form": form})

        if User.objects.filter(username=form["username"]).exists():
            form["errors"] = "Пользователь с таким логином уже существует"
            return render(request, "register.html", {"form": form})

        user = User.objects.create_user(
            username=form["username"],
            password=form["password"]
        )

        login(request, user)
        return redirect("archive")

    return render(request, template_name, {})
