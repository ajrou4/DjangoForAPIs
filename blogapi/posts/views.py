from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly # Assuming you have a custom permission class


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # Use your custom permission class
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)  # Use your custom permission class
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# Create your views here.
