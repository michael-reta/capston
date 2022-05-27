from django.urls import path
from . import views

app_name = "quickstart_app"

urlpatterns = [
    path('index/', views.index, name='index'),
    path("testing/", views.testing, name='testing'),
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('posts/', views.blog_posts, name = 'posts'),
    path('add/', views.add_post, name = 'add_posts'),
]