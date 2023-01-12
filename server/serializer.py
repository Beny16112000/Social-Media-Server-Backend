from rest_framework import serializers
from .models import Profile, ProfileWork, ProfileStudy, Friends, Group, GroupManager, GroupManagerRequest, GroupMembersRequest, GroupPost, GroupPostComment, FeedPost


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'public',
            'gender',
            'birthday',
            'phone',
            'living'
        ]



class ProfileWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileWork
        fields = [
            'id',
            'user',
            'workplace',
            'start',
            'end',
            'detail'
        ]



class ProfileStudySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileStudy
        fields = [
            'id',
            'user',
            'institution',
            'start',
            'end',
            'detail'
        ]



class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = [
            'id',
            'sender',
            'friends'
        ]

    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['sender'] = instance.sender.username
        return data



class GroupsYouManageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupManager
        fields = [
            'id',
            'group',
            'super_manager'
        ]


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['group'] = instance.group.name
        return data



class GroupManagersRequestsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupManagerRequest
        fields = [
            'id',
            'group'
        ]



class GroupMembersRequestsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GroupMembersRequest
        fields = [
            'id',
            'user'
        ]


    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.username
        return data



class GroupPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPost
        fields = [
            'id',
            'group',
            'content',
            'created_at',
        ]



class GroupPostsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPostComment
        fields = [
            'id',
            'user',
            'post',
            'comment'
        ]



class FeedPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPost
        fields = [
            'id',
            'user',
            'content',
            'created_at'
        ]


