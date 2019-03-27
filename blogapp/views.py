from django.shortcuts import render
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

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
