from rest_framework import routers

from django.urls import include, path

from .views import (CommentViewSet, FollowViewSet,
                    GroupViewSet, PostViewSet)


router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='post-comments')
router_v1.register('follow', FollowViewSet, basename='follows')
router_v1.register('groups', GroupViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
