from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer



class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

    pass


<<<<<<< HEAD
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
=======
class PostDetail(generics.RetrieveAPIView):
>>>>>>> origin/master
    queryset = Post.objects.all()
    serializer_class = PostSerializer

