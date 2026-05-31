from django.urls import path
from ..views.comment_views import PostCommentListCreateView, CommentDetailView

urlpatterns = [
    path('<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]