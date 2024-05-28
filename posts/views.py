from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from posts.models import Post


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'


class NewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'text']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

