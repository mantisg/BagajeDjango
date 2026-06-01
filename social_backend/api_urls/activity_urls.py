from django.urls import path
from ..views.activity_views import MyActivityView

urlpatterns = [

    path(
        'users/me/activity/',
        MyActivityView.as_view(),
        name='my-activity'
    ),
]