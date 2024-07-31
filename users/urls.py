from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('profile/<int:pk>', views.UserProfileDetail.as_view(), name='profile'),
    path('profile/<int:pk>/delete/', views.DeleteProfile.as_view(), name='delete_profile'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]
