from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post



class PostSimpleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Sarlavha kamida 5 ta belgidan iborat bo'lishi shart!")
        return value

    def validate(self, attrs):
        title = attrs.get('title', '')
        content = attrs.get('content', '')
        if title.lower() in content.lower() and len(content) < 15:
            raise serializers.ValidationError("Maqola matni faqat sarlavhaning o'zidan iborat bo'lib qolmasligi kerak.")
        return attrs
