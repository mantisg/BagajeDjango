from .models import UserActivity


def log_activity(
    user,
    post,
    activity_type
):

    UserActivity.objects.create(
        user=user,
        post=post,
        activity_type=activity_type
    )