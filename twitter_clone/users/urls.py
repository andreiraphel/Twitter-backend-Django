from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('users', views.users, name='users'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('<str:username>', views.details, name='details'),
    path('<int:object_id>/likes', views.liked, name='liked'),
    path('<int:object_id>/comments', views.comments, name='comments'),
]
