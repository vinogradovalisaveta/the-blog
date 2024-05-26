from django.urls import path
from users import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.UserRegisterView.as_view(), name='signup'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name='profile'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]
