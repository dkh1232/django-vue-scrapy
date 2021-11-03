from rest_framework import serializers
from comment.models import Comment,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]

class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserSerializer(read_only=True)

    # movie = serializers.HyperlinkedIdentityField(view_name= 'movie-detail',read_only=True)
    # movie_id = serializers.IntegerField(write_only= True,allow_null=False,required=True)


    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}