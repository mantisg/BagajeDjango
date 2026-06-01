from django.urls import path, include

urlpatterns = [
    path(
        'auth/',
        include('social_backend.api_urls.auth_urls')
    ),

    path(
        '',
        include('social_backend.api_urls.post_urls')
    ),

    path(
        'comments/',
        include('social_backend.api_urls.comment_urls')
    ),

    path(
        'users/',
        include('social_backend.api_urls.user_urls')
    ),
    path(
        '',
        include('social_backend.api_urls.saved_post_urls')
    ),
    path(
        '',
        include('social_backend.api_urls.activity_urls')
    ),
]