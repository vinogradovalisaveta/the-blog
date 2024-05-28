from django.views.generic import CreateView, ListView, DetailView
from posts.models import Post


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'


class NewPost(CreateView):
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

