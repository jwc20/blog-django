from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fieleds = ("id", "author", "title", "body", "created_at")
        model = Post
