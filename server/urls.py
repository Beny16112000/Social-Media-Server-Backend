from django.urls import path
from . import views


# Url's


urlpatterns = [
    path('auth/',views.Authentication.as_view({'post': 'create'})),
    path('auth/login',views.Authentication.as_view({'post': 'login'})),
    path('auth/logout',views.Authentication.as_view({'post': 'logout'})),
    path('profile/',views.Profile.as_view({'get': 'list', 'post': 'create'})),
    path('profile/update',views.Profile.as_view({'post': 'update'})),
    path('profile/<int:id>',views.Profile.as_view({'delete': 'destroy'})),
    path('profile/work/',views.ProfileWork.as_view({'post': 'create', 'get': 'list'})),
    path('profile/work/<int:id>',views.ProfileWork.as_view({'delete': 'destroy'})),
    path('profile/study/',views.ProfileStudy.as_view({'post': 'create', 'get': 'list'})),
    path('profile/study/<int:id>',views.ProfileStudy.as_view({'delete': 'destroy'})),
    path('friend/',views.FriendRequests.as_view({'post': 'create', 'get': 'list'})),
    path('friend/<int:id>',views.FriendRequests.as_view({'put': 'update', 'delete': 'destroy'})),
    path('friend/all/',views.FriendsAll.as_view()),
    path('friend/all/<int:id>',views.FriendsAll.as_view()),
    path('group/',views.GroupManagment.as_view({'post': 'create', 'get': 'list', 'put': 'create'})),
    path('group/<int:id>',views.GroupManagment.as_view({'put': 'update', 'delete': 'destroy'})),
    path('group/manager/',views.GroupManagerRequest.as_view()),
    path('group/manager/<int:id>',views.GroupManagerRequest.as_view()),
    path('group/friend/',views.GroupMembers.as_view({'post': 'create', 'get': 'list'})),
    path('group/friend/<int:id>',views.GroupMembers.as_view({'put': 'update', 'delete': 'destroy'})),
    path('group/<str:name>/', views.GroupPosts.as_view({'post': 'create', 'get': 'list'})),
    path('group/<str:name>/<int:id>', views.GroupPosts.as_view({'put': 'update', 'delete': 'destroy'})),
    path('group/like/<str:name>/<int:id>/',views.GroupPostLike.as_view({'post': 'create', 'get': 'list'})),
    path('group/comment/<str:name>/<int:id>/',views.GroupPostComment.as_view({'post': 'create', 'get': 'list', 'delete': 'destroy'})),
    path('feed/post/',views.FeedPost.as_view({'post': 'create', 'get': 'list'})),
    path('feed/post/<int:id>',views.FeedPost.as_view({'put': 'update', 'delete': 'destroy'})),
    path('feed/',views.Feed.as_view())
]

