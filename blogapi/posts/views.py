from rest_framework import generics
from django.contrib.auth import get_user_model # Import the custom user model if you have one, otherwise use the default User model
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly # Assuming you have a custom permission class
from rest_framework.permissions import IsAdminUser  


class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser]  # Only admin users can access this view
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer