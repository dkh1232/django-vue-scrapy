from rest_framework import serializers
from ygdy.models import User,Movie
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from comment.serializers import CommentSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    id =serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Movie
        fields =[
            'title',
            'img',
            'tran_name',
            'title',
            'year',
            'country',
            'douban_rate',
            'language',
            'publish_date',
            'movie_time',
            'director',
            'main_actor',
            'download_url',
            'created',
            'id',
            'comments'
        ]

class UserRgisterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')
    class Meta:
        model = User
        fields  = [
            'id',
            'url',
            'username',
            'password',
        ]
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'last_name',
            'first_name',
            'last_login',
            'date_joined',
        ]

