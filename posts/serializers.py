from rest_framework import serializers
from posts.models import Post, Comment
from django.contrib.auth import get_user_model


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')
    image=serializers.ImageField(max_length=None)
    comments = serializers.StringRelatedField(many=True,read_only=True)


    class Meta:
        model = Post
        fields = ('url', 'id', 'highlight', 'owner','image','title', 'content','name','subscribe', 'draft','subscribers','likes','comments')
'''
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='comment-highlight', format='html')

    class Meta:
        model = Comment
        fields = ('url','id','highlight','owner','post','author','likes')

    
'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts= serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    #name = serializers.CharField(max_length=200)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(write_only=True)
    #comments = serializers.CharField(max_length=200)

    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'posts','password','email')

    def create(self, validated_data):
        """
        Create and return a new `posts` instance, given the validated data.

        """
        user = get_user_model().objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    
