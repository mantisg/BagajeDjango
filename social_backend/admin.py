from django.contrib import admin
from .models import Post, User, Comment, Reaction, UserActivity

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(UserActivity)