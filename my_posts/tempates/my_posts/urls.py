from django.urls import path
from . import views
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

app_name = 'my_posts'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]


