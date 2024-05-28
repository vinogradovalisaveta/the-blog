from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostListView.as_view, name='index'),
    path('new_post', views.NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post')
]
