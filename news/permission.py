from rest_framework import permissions

class IsApiNewsItem(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the request is for the 'update' or 'destroy' action
        if view.action in ['update', 'destroy']:
            news_item = view.get_object()
            return news_item.added_through_api
        return True
