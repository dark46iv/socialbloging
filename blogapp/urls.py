from django.urls import path
from .views import PostListView, PostDetailView, AuthorListView, index, post_new

urlpatterns = [
    path('', index, name='index'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post_new/', post_new, name='post-new'),
    path('authors/', AuthorListView.as_view(), name='authors')
    ]