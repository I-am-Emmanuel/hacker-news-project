# from django.shortcuts import render
from .serializer import NewsItemSerializer, NewsItemUpdateSerializer
from .paginator import *
from .models import NewsItem
from .permission import IsApiNewsItem

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status


from django_filters.rest_framework import DjangoFilterBackend

from django.http import HttpResponse




class NewsItemViewSet(viewsets.ModelViewSet):
    queryset = NewsItem.objects.all()
    http_method_names = ['get', 'post','put', 'delete']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = DefaultPagination
    filterset_fields = ['title', 'points']
    search_fields = ['points', 'title']


    def create(self, request, *args, **kwargs):
        user = request.user
        # if user.is_staff:
        # serializer = NewsItemSerializer(data=request.data, context={'user_id': self.request.user.id})
        serializer = NewsItemSerializer(data=request.data, context={'user_id': self.request.user.id})
        
        serializer.is_valid(raise_exception=True)
        news = serializer.save(added_through_api=True)
        serializer = NewsItemSerializer(news)
        return Response(serializer.data)
        # return Response({'message': 'You have no permission to add a news'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def get_serializer_class(self):
        # user = request.user
        if self.request.method == 'POST':
            return NewsItemSerializer
        elif self.request.method == 'PUT':
            return NewsItemUpdateSerializer
        return NewsItemSerializer

         

    def delete(self, request, *args, **kwargs):
        # user = request.user
        # if user.is_staff:
        return Response({'message': 'news deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        # else:
            # return Response({'error': 'News cannot be deleted.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            return [IsApiNewsItem()]
        return super().get_permissions()


