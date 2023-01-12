from django.contrib import admin
from .models import Profile, ProfileWork, ProfileStudy, Friends, Group, GroupManager, GroupMembers, GroupMembersRequest, GroupManagerRequest, GroupPost, GroupPostLike, GroupPostComment, FeedPost


# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone','public')
admin.site.register(Profile, ProfileAdmin)


class ProfileWorkAdmin(admin.ModelAdmin):
    list_display = ('user',)
admin.site.register(ProfileWork, ProfileWorkAdmin)


class ProfileStudyAdmin(admin.ModelAdmin):
    list_display = ('user',)
admin.site.register(ProfileStudy, ProfileStudyAdmin)


class FriendsAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','friends')
admin.site.register(Friends, FriendsAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('created_by','name')
admin.site.register(Group, GroupAdmin)


class GroupManagerAdmin(admin.ModelAdmin):
    list_display = ('manager','group')
admin.site.register(GroupManager, GroupManagerAdmin)


class GroupMembersRequestAdmin(admin.ModelAdmin):
    list_display = ('user','group')
admin.site.register(GroupMembersRequest, GroupMembersRequestAdmin)


class GroupMembersAdmin(admin.ModelAdmin):
    list_display = ('user','group')
admin.site.register(GroupMembers, GroupMembersAdmin)


class GroupManagerRequestAdmin(admin.ModelAdmin):
    list_display = ('user','group')
admin.site.register(GroupManagerRequest, GroupManagerRequestAdmin)


class GroupPostAdmin(admin.ModelAdmin):
    list_display = ('user','group','created_at')
admin.site.register(GroupPost, GroupPostAdmin)


class GroupPostLikeAdmin(admin.ModelAdmin):
    list_display = ('user','post')
admin.site.register(GroupPostLike, GroupPostLikeAdmin)


class GroupPostCommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','comment')
admin.site.register(GroupPostComment, GroupPostCommentAdmin)


class FeedPostAdmin(admin.ModelAdmin):
    list_display = ('user','created_at')
admin.site.register(FeedPost, FeedPostAdmin)