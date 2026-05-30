from django.urls import path
from ..views.reaction_views import ToggleReactionView

url_patterns = [
    path('posts/<int:post_id>/react/', ToggleReactionView.as_view(), name='toggle-reaction'),
]