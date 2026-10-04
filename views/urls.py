from django.urls import path
from .views import PostListCreateView, PostDetailApiView

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailApiView.as_view(), name="post-detail"),
]

