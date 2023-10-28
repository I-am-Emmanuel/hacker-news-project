from django.urls import path, include
from .views import *
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register(r'api-news', NewsItemViewSet, basename='hacknews')

urlpatterns = [
    path('', include(router.urls)),
]