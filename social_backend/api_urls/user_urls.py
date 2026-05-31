from django.urls import path
from ..views.user_views import (
    CurrentUserView,
    UserProfileView,
)

urlpatterns = [

    path(
        'me/',
        CurrentUserView.as_view(),
        name='current-user'
    ),

    path(
        '<slug:slug>/',
        UserProfileView.as_view(),
        name='user-profile'
    ),
]