from rest_framework import serializers
from django.contrib.auth import get_user_model # Import the custom user model
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'created_at',]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ('id', 'username',)  # Adjust fields as necessary
        