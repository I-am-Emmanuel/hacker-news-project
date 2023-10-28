from rest_framework import serializers
from . models import NewsItem

class NewsItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['id','title', 'url', 'points', 'author','comments', 'created_at']
        extra_kwargs = {
            'created_at': {'read_only': True},
            'comments' : {'read_only': True},
            'points' : {'read_only': True},
        }
    def vote(self):
        self.instance.points += 1
        self.instance.save()


class NewsItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsItem
        fields = ['title', 'author', 'url' ]
