from django.urls import path
from users import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.UserRegisterView.as_view(), name='signup'),
    path('profile/<int:pk>', views.ProfileEdit.as_view(), name='profile'),
]
