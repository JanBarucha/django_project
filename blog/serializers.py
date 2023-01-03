from rest_framework import serializers
from blog.models import Post,GameBoard



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']

"""id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance
"""

class GameBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameBoard
        fields = [
            'id',
            'title',
            'score'
        ]
