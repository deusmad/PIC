from django.contrib import admin
from django.urls import path
from articles.views import archive, get_article, create_post, user_login, user_logout

urlpatterns = [
    path('', archive, name='archive'),
    path('article/new/', create_post, name='create_post'),
    path('article/<int:article_id>/', get_article, name='get_article'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('admin/', admin.site.urls),
]