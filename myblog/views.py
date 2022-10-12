from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
@login_required
def homepage(request):
    context = {
        "posts" : Post.objects.all(),
        "title" : "Main",
    }
    return render(request, 'blog-templates/home.html', context)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog-templates/home.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 10

class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog-templates/user_posts.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog-templates/view_post.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "blog-templates/create_post.html"
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "blog-templates/create_post.html"
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog-templates/delete_post.html"
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required
def about(request):
    context = {
        "title" : "About",
    }
    return render(request, 'blog-templates/about.html', context)