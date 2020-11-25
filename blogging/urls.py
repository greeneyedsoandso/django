from django.urls import path
from blogging.views import PostListView, PostDetailView, CommentCreateView

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("add/", CommentCreateView.as_view(), name="add_post"),
]
