from django.conf import settings
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)  # Short title (max 50 characters)
    body = models.TextField()  # Main content of the post (unlimited length)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Links to your custom or default User model
        on_delete=models.CASCADE   # Delete posts if the user is deleted
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Set only when created
    updated_at = models.DateTimeField(auto_now=True)      # Update on each save

    def __str__(self):
        return self.title  # Readable string representation of the post
