from django.shortcuts import render, redirect
from .models import Post, Profile, PostInstance
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from .forms import PostForm
from django.utils import timezone

# Create your views here.


def index(request):

    return render(request, 'index.html', context={})


class PostListView(ListView):

    model = Post
    paginate_by = 5

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['posts'] = self.model.objects.all()
        return context


class PostDetailView(DetailView):

    model = Post


class AuthorListView(ListView):

    model = Profile
    paginate_by = 10

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(AuthorListView, self).get_context_data(*args, **kwargs)
        context['authors'] = self.model.objects.all()
        return context


def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


class AuthorPostListView(PostListView):
    model = Post
    template_name = 'blogapp/post_list.html'

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
