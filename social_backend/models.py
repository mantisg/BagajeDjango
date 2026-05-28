from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image
from io import BytesIO
from django.core.files import File

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    media = models.FileField(upload_to='posts/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.media:
            img = Image.open(self.media)
            max_size = (800, 800)
            img.thumbnail(max_size, Image.ANTIALIAS)
            img.save(self.media.path, quality=85, optimize=True)

    def __str__(self):
        return self.title
    
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email = models.EmailField(unique=True)
    is_creator = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)