from django.urls import path
from posts import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('new_post', views.NewPost.as_view(), name='new_post'),
    path('post/<int:pk>/', views.post_detail, name='post'),
    # path('post/<int:pk>/', views.PostDetail.as_view(), name='post'),
    path('post/<int:pk>/edit', views.EditPostView.as_view(), name='edit'),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name='delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/like', views.like_post, name='like_post'),
]
