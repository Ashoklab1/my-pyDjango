from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item, Post
from django.shortcuts import render
from my_posts.models import Post
from django.core.paginator import Paginator


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'my_posts/post_list.html', {'page_obj': page_obj})
def homepage(request):
    posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'homepage.html', {'posts': posts})

def home(request):
    return render(request, 'home.html')
class ItemListView(ListView):
    model = Item
    template_name = '{app}/item_list.html'

class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'description']
    template_name = '{app}/item_form.html'
    success_url = reverse_lazy('{app}_list')

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'description']
    template_name = '{app}/item_form.html'
    success_url = reverse_lazy('{app}_list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = '{app}/item_confirm_delete.html'
    success_url = reverse_lazy('{app}_list')
    

class PostListView(ListView):
    model = Post
    template_name = 'my_posts/post_list.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'my_posts/post_form.html'
    success_url = reverse_lazy('my_posts:list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'my_posts/post_form.html'
    success_url = reverse_lazy('my_posts:list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'my_posts/post_confirm_delete.html'
    success_url = reverse_lazy('my_posts:list')