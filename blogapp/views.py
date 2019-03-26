from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

# Create your views here.


def index(request):
    return render(request, 'index.html', context={})


class PostListView(ListView):

    model = Post
    template_name = 'index.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['posts'] = self.model.objects.all()
        return context

