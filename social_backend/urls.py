from django.urls import path, include

urlpatterns = [
    path(
        'auth/',
        include('social_backend.urls.auth_urls')
    ),

    path(
        '',
        include('social_backend.urls.post_urls')
    ),

    path(
        'comments/',
        include('social_backend.urls.comment_urls')
    ),

    path(
        'users/',
        include('social_backend.urls.user_urls')
    ),
]