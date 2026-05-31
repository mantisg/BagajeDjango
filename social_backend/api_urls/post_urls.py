from rest_framework.routers import DefaultRouter
from django.urls import path
from ..views.post_views import PostViewSet
from ..views.comment_views import PostCommentListCreateView

router = DefaultRouter()

router.register(
    r'posts',
    PostViewSet,
    basename='post'
)

urlpatterns = router.urls + [

    path(
        'posts/<slug:slug>/comments/',
        PostCommentListCreateView.as_view(),
        name='post-comments'
    ),

]