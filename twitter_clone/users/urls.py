from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('users/', views.users, name='users'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('users/details/<int:user_id>', views.details, name='details'),
    path('users/details/<int:user_id>/<int:object_id>/likes', views.liked, name='liked'),
    path('users/details/<int:user_id>/<int:object_id>/comments', views.comments, name='comments'),
]
