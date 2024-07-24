from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from posts.models import Post, Comment
from posts.forms import CommentForm


@login_required
@require_POST
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
        return redirect('post', pk=pk)
    return render(request, 'comment.html',
                  {'post': post,
                   'form': form})


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class EditPostView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'text', 'image']
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.pk})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    return render(request, 'post.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'post.html'


class NewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = ['title', 'text', 'image']

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

