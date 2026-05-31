from django.urls import path
from ..views.saved_post_views import (
    ToggleSavedPostView,
    SavedPostListView,
)

urlpatterns = [

    path('posts/<int:post_id>/save/', ToggleSavedPostView.as_view(), name='toggle-save-post'),
    path('users/me/saved-posts/', SavedPostListView.as_view(), name='saved-posts'),
]