from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/details/<int:user_id>', views.details, name='details'),
    path('users/details/<int:user_id>/<int:object_id>/likes', views.liked, name='liked'),
    path('users/details/<int:user_id>/<int:object_id>/comments', views.comments, name='comments'),
]