from django.contrib import admin
from django.urls import path
from articles.views import (
    archive,
    get_article,
    create_post,
    user_login,
    user_logout,
    user_registration
)

urlpatterns = [
    path('', archive, name='archive'),
    path('article/new/', create_post, name='create_post'),
    path('article/<int:pk>/', get_article, name='get_article'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_registration, name='registration'),
    path('admin/', admin.site.urls),
]