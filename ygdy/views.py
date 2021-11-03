from django.shortcuts import render
from rest_framework import viewsets,mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly,BasePermission,AllowAny,IsAuthenticated
from .permissions import IsSelfOrReadOnly
from ygdy.models import Movie,User
from ygdy.serializers import MovieSerializer,UserRgisterSerializer,UserDetailSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from django.contrib.auth.backends import ModelBackend
# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = []
    queryset = Movie.objects.all().order_by('id')
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,]
    search_fields =['title','year','country']
     # http://127.0.0.1:8000/api/movie/

class MovieViewSet1(viewsets.ModelViewSet):#国产
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = []
    queryset = Movie.objects.filter(Q(country="['中国大陆']") | Q(country="['中国香港']")| Q(country="['中国大陆,中国香港']")| Q(country="['中国大陆,中国台湾']")).order_by('-douban_rate')
    serializer_class = MovieSerializer
# http://127.0.0.1:8000/api/oumei/

class MovieViewSet2(viewsets.ModelViewSet):#欧美
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = []
    queryset = Movie.objects.filter(Q(country="['美国']") | Q(country="['美国,英国']")| Q(country="['加拿大']")).order_by('-id')
    serializer_class = MovieSerializer
# http://127.0.0.1:8000/api/oumei/

class MovieViewSet3(viewsets.ModelViewSet):#日韩
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = []
    queryset = Movie.objects.filter(Q(country="['日本']") | Q(country="['韩国']")).order_by('id')
    serializer_class = MovieSerializer
# # http://127.0.0.1:8000/api/rihan/


class MovieViewSet4(viewsets.ModelViewSet):#最新
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = []
    queryset = Movie.objects.filter(year ="['2021']")
    serializer_class = MovieSerializer

class MovieViewSet5(viewsets.ModelViewSet):#gaofen
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = []
    queryset = Movie.objects.order_by('-douban_rate')
    serializer_class = MovieSerializer
 # input(http://127.0.0.1:8000/api/gaofen/?page=8052)



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRgisterSerializer
    lookup_field = 'username'
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]
        return super().get_permissions()

    @action(detail=True, methods=['get'])
    def info(self, request, username=None):
        queryset = User.objects.get(username=username)
        serializer = UserDetailSerializer(queryset, many=False)
        return Response(serializer.data)

    @action(detail=False)
    def sorted(self, request):
        users = User.objects.all().order_by('-username')
        page = self.paginate_queryset(users)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)

