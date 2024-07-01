from django.urls import path
from .views import get_all, get, create, update, delete

# Create url pattern for displaying a list of all posts
# Create url pattern for displaying details of a specific post
# Create url pattern for creating a new post
# Create url pattern for updating an existing post
# Create url pattern for deleting an existing post

urlpatterns = [
    path('', get_all, name='stickynotes'),
    path('<int:pk>/', get, name='stickynote'),
    path('new/', create, name='create_stickynote'),
    path('<int:pk>/edit/', update, name='update_stickynote'),
    path('<int:pk>/delete/', delete, name='delete_stickynote'),
]
