from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name='profile'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]
