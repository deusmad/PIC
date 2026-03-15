from .models import Article
from django.shortcuts import render, get_object_or_404


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
