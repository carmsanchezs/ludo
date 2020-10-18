"""Posts URLS."""

# Django
from django.urls import path

# Views
from posts import views


urlpatterns = [

    path(
        route='', 
        view=views.list_posts, 
        name='list_posts'
    ),

    path(
        route='detail/<int:pk>',
        view=views.detail_post,
        name='detail'
    )

]
