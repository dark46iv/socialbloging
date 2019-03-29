from django.urls import path
from .views import PostListView, PostDetailView, AuthorListView, AuthorPostListView, index, post_new

urlpatterns = [
    path('', index, name='index'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post_new/', post_new, name='post-new'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('author_posts/<pk>/', AuthorPostListView.as_view(), name='author-posts'),
    path('my_posts/', AuthorPostListView.as_view(), name='my-posts'),
    ]