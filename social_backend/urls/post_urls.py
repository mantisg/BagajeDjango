from rest_framework.routers import DefaultRouter
from ..views.post_views import PostViewSet

router = DefaultRouter()

router.register(
    r'posts',
    PostViewSet,
    basename='post'
)

urlspatterns = router.urls