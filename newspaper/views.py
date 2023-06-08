from django.urls import resolve
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import NewsForm
from .filters import PostFilter
from .models import Post, Category, SubscribedUsersCategory
from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
# from django.core.mail import send_mail
# from django.core.paginator import Paginator
# from django.contrib.auth.mixins import LoginRequiredMixin


class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10


class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class PostsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        return context

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        qs = self.get_filter().qs
        return qs


class PostsAdd(PermissionRequiredMixin, CreateView):
    permission_required = ('newspaper.add_post', )
    template_name = 'add.html'
    form_class = NewsForm
    success_url = '/news/'

# -----


class PostEdit(PermissionRequiredMixin, UpdateView):
    permission_required = ('newspaper.change_post', )
    template_name = 'edit.html'
    form_class = NewsForm
    success_url = '/news/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('newspaper.delete_post', )
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class PostCategoryView(ListView):
    model = Post
    template_name = 'news/category.html'
    context_object_name = 'posts'
    ordering = ['-dateCreated']
    paginate_by = 10

    def get_queryset(self):
        self.id = resolve(self.request.path_info).kwargs['pk']
        c = Category.objects.get(id=self.id)
        queryset = Post.objects.filter(category=c)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        category = Category.objects.get(id=self.id)
        subscribed = category.subscribers.filter(email=user.email)
        if not subscribed:
            context['category'] = category

        return context


def subscription(request):
    category_id = request.GET.get('category_id')
    print(category_id)
    category = Category.objects.get(id=category_id)

    if not category.subscribed_users.filter(email=request.user.email).exists():
        user = request.user
        SubscribedUsersCategory.objects.create(
            subscribed_users=user, category=category)
    return redirect(request.META.get('HTTP_REFERER',
                                     'redirect_if_referer_not_found'))


def home(request):
    return render(request, 'home.html')
