from .models import Article
from .form import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


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
