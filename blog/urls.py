from django.urls import path, include
from blog import views
from blog.api import  viewsets

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk>/', views.Post.as_view(),name='post'),
    path('post/new/', views.CreatePost.as_view(), name='create_post'),
    path('post/edit/<int:pk>', views.CreatePost.as_view(), name='create_post'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('post/<int:pk>/comment/', views.Comment, name='comment_frame'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='perfil'),
    path('api/v0/posts/', viewsets.posts_view, name='api_posts'),

]
