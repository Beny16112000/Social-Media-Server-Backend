from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action, permission_classes
from .User.auth import UserTest, UserClass
from .User.profile import ProfileClass, WorkNstudy
from .serializer import ProfileSerializer, ProfileWorkSerializer, ProfileStudySerializer, FriendsSerializer, GroupsYouManageSerializer, GroupManagersRequestsSerializers, GroupMembersRequestsSerializers, GroupPostsSerializer, GroupPostsCommentSerializer, FeedPostsSerializer
from django.http import JsonResponse
from .Friends.friends import FriendsClass
from rest_framework.views import APIView
from .Groups.managment import GroupsManagmentClassTest
from .Groups.requests import ManagerRequest, GroupMembersClass
from .Groups.posts import GroupPostsClass, GroupPostLikeClass, GroupPostCommentClass
from .Feed.posts import FeedPostClass
from .Feed.feed import FeedAlgorithm


# Superuser: Usename - benny, Password - 1234. Token - 81c5e6d2c5cbd373153a793663c51c516ef9671d


class Authentication(viewsets.ModelViewSet):
    """
    Authentication Class take care of register, login, logout, delete user
    """
    def create(self, request):
        data = JSONParser().parse(request)
        user = UserTest().register(data['username'],data['firstName'],data['lastName'],data['email'],data['pass1'],data['pass2'])
        if user is True:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(user, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=True, methods=['post'])
    def login(self, request):
        data = JSONParser().parse(request)
        user = UserTest().login(data['username'],data['password'])
        if type(user) is not dict:
            return Response(user.key, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(user, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=True, methods=['post'])
    def logout(self, request):
        process = UserClass().logout(request.user)
        return Response(process, status=status.HTTP_202_ACCEPTED)

    
    def destroy(self, request, pk):
        user = UserTest().delete(request.user, pk)
        if user is True:
            return Response('User deleted', status=status.HTTP_200_OK)
        else:
            return Response(user, status=status.HTTP_400_BAD_REQUEST)



class Profile(viewsets.ModelViewSet):
    """
    Create Profile
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = JSONParser().parse(request)
        profile = ProfileClass().main(request.user,data['public'],
                                    data['gender'],data['birthday'],int(data['phone']),data['living'])
        if profile is True:
            return Response(status=status.HTTP_201_CREATED)
        else:   
            return Response(profile, status=status.HTTP_400_BAD_REQUEST)
    
    
    def list(self, request):
        data = ProfileClass().get(request.user)
        dataWork = ProfileClass().getWork(request.user)
        dataStudy = ProfileClass().getStudy(request.user)
        serializerProfile = ProfileSerializer(data)
        serializerWork = ProfileWorkSerializer(dataWork, many=True)
        serializerStudy = ProfileStudySerializer(dataStudy, many=True)
        return JsonResponse({'Profile': {'data': serializerProfile.data, 'work': serializerWork.data, 'study': serializerStudy.data}}, status=status.HTTP_200_OK)


    @action(detail=True, methods=['post'])
    def update(self, request):
        data = JSONParser().parse(request)
        ProfileClass().update(request.user,data['public'],
                            data['gender'],data['birthday'],int(data['phone']),data['living'])
        return Response('Updated', status=status.HTTP_200_OK)
        

    def destroy(self, request, id):
        ProfileClass().delete(id)
        return Response(status=status.HTTP_200_OK)
    
    

class ProfileWork(viewsets.ModelViewSet):
    """
    More additional info for the profile section - Work
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = JSONParser().parse(request)
        work = WorkNstudy().create(request.user, data['workplace'], data['start'], data['end'], data['detail'], 1)
        if work is not None:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
    def list(self, request):
        work = WorkNstudy().get(request.user,1)
        serializer = ProfileWorkSerializer(work, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def destroy(self, request, id):
        WorkNstudy().delete(id, 1)
        return Response(status=status.HTTP_200_OK)



class ProfileStudy(viewsets.ModelViewSet):
    """
    More additional info for the profile section - Study
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = JSONParser().parse(request)
        study = WorkNstudy().create(request.user, data['institution'], data['start'], data['end'], data['detail'], 2)
        if study is not None:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        
    def list(self, request):
        work = WorkNstudy().get(request.user,2)
        serializer = ProfileStudySerializer(work, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def destroy(self, request, id):
        WorkNstudy().delete(id, 2)
        return Response(status=status.HTTP_200_OK)



class FriendRequests(viewsets.ModelViewSet):
    """
    Friend request handle
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = JSONParser().parse(request)
        friends = FriendsClass().send(request.user, data['receiver'])
        if friends is not None:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
    def list(self, request):
        friends = FriendsClass().list(request.user)
        serializer = FriendsSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, id):
        friend = FriendsClass().accept(request.user,id)
        serializer = FriendsSerializer(friend)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def destroy(self, request, id):
        FriendsClass().delete(request.user, id)
        return Response(status=status.HTTP_200_OK)



class FriendsAll(APIView):
    """
    Get All Friends and delete Friendship
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = FriendsClass().all(request.user)
        serializer = FriendsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def delete(self, request, id):
        remove = FriendsClass().delete_friendship(request.user, id)
        if remove is not None:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



class GroupManagment(viewsets.ModelViewSet):
    """
    Create and manage Group
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = JSONParser().parse(request)
        group = GroupsManagmentClassTest().create(request.user, data['name'], data['about'])
        if group is True:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def list(self, request):
        groups = GroupsManagmentClassTest().get(request.user)
        serializer = GroupsYouManageSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, id):
        data = JSONParser().parse(request)
        GroupsManagmentClassTest().update(request.user, data['name'], data['about'], id)
        return Response(status=status.HTTP_200_OK)

    
    def destroy(self, request, id):
        group = GroupsManagmentClassTest().delete(request.user, id)
        if group is True:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    

class GroupManagerRequest(APIView):
    """
    Handle Group Manager Request
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = JSONParser().parse(request)
        request = ManagerRequest().send(request.user, data['receiver'], data['group'])
        if request != 404:
            return Response(status=status.HTTP_201_CREATED) 
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
    def get(self, request):
        data = ManagerRequest().get(request.user)
        serializer = GroupManagersRequestsSerializers(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def put(self, request, id):
        add = ManagerRequest().update(request.user, id)
        if add is True:
            return Response(status=status.HTTP_200_OK)

    
    def delete(self, request, id):
        remove = ManagerRequest().delete(request.user, id)
        if remove:
            return Response(status=status.HTTP_202_ACCEPTED)



class GroupMembers(viewsets.ModelViewSet):
    """
    Manage | Display - Group Friends and request
    """
    permission_classes = [IsAuthenticated]

    # Send friend request To Group
    def create(self, request): 
        data = JSONParser().parse(request)
        add = GroupMembersClass().send(request.user, data['group'])
        if add is True:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    

    # Display of friend request to group
    def list(self, request):
        data = JSONParser().parse(request)
        requests = GroupMembersClass().view(request.user, data['group'])
        serializer = GroupMembersRequestsSerializers(requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, id):
        GroupMembersClass().update(id)
        return Response(status=status.HTTP_200_OK)


    def destroy(self, request, id):
        GroupMembersClass().delete(id)
        return Response(status=status.HTTP_200_OK)


class GroupPosts(viewsets.ModelViewSet):
    """
    Group posts handle 
    """
    permission_classes = [IsAuthenticated]

    def create(self, request, name):
        data = JSONParser().parse(request)
        add = GroupPostsClass().add(request.user, name, data['content'])
        if add is True:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
    def list(self, request, name):
        posts = GroupPostsClass().get_posts(name)
        serializer = GroupPostsSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def update(self, request, name, id):
        data = JSONParser().parse(request)
        post = GroupPostsClass().update(id, request.user, name, data['content'])
        if post is True:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, name, id):
        post = GroupPostsClass().delete(id, request.user, name)
        if post is True:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class GroupPostLike(viewsets.ModelViewSet):
    """
    Group likes on posts
    """
    permission_classes = [IsAuthenticated]

    # Also Create like and delete like, I identify by if the like exists
    def create(self, request, **kwargs):
        GroupPostLikeClass(request.user, kwargs['id']).identify()
        return Response(status=status.HTTP_200_OK)


    def list(self, request, **kwargs):
        print(kwargs['id'])
        likes = GroupPostLikeClass(request.user, kwargs['id']).likes()
        return JsonResponse({
            'post': kwargs['name'],
            'likes': likes
        })



class GroupPostComment(viewsets.ModelViewSet):
    """
    Group comments on posts
    """
    permission_classes = [IsAuthenticated]

    def create(self, request, **kwargs):
        data = JSONParser().parse(request)
        comment = GroupPostCommentClass().comment(request.user,kwargs['id'],data['comment'])
        if comment:
            return Response(status=status.HTTP_201_CREATED)

    
    def list(self, request, **kwargs):
        comments = GroupPostCommentClass().comments(kwargs['id'])
        if comments:
            serializer = GroupPostsCommentSerializer(comments, many=True)
            return JsonResponse({
                'post': kwargs['id'],
                'comment': serializer.data
            })


    def destroy(self, request, **kwargs):
        data = JSONParser().parse(request)
        comment = GroupPostCommentClass().delete(request.user, kwargs['id'])
        if comment:
            return Response(status=status.HTTP_200_OK)



class FeedPost(viewsets.ModelViewSet):
    """
    Private posts to feed
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        data = JSONParser().parse(request)
        post = FeedPostClass().create(request.user, data['content'])
        return Response(status=status.HTTP_201_CREATED)

    
    def list(self, request):
        posts = FeedPostClass().view(request.user)
        if not posts:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = FeedPostsSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    
    def update(self, request, **kwargs):
        data = JSONParser().parse(request)
        post = FeedPostClass().update(request.user, data['content'], kwargs['id'])
        if post:
            return Response(status=status.HTTP_200_OK)

    
    def destroy(self, request, **kwargs):
        post = FeedPostClass().delete(request.user, kwargs['id'])
        if post is True:
            return Response(status=status.HTTP_200_OK)



class Feed(APIView):
    """
    Feed
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = FeedAlgorithm().algorithm(request.user)
        return Response(posts, status=status.HTTP_200_OK)



