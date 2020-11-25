from django.urls import path
from blogging.views import PostListView, PostDetailView, CommentDetailView

urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    path("comment/", CommentDetailView.add_model, name="add_post"),
]
