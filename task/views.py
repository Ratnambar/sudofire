from django.shortcuts import render
from django.http import JsonResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs
from .models import Task
from django.views.generic import CreateView,ListView
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


class PostCreateView(CreateView):
    template_name = 'task/post.html'
    form_class = PostForm
    success_url = reverse_lazy('lists')


class PosListView(ListView):
    queryset = Task.objects.all()
    template_name = 'task/index.html'
    context_object_name = 'posts'


# First Question
def get_parameter(request):
    url = 'http://foo.appspot.com/abc?def=my-parameter'
    parsed = urlparse.urlparse(url)
    print(parse_qs(parsed.query)['def'])
    return JsonResponse(parse_qs(parsed.query)['def'], safe=False)


