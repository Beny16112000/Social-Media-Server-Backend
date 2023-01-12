from ..models import GroupPost, Group, GroupMembers, GroupManager, GroupPostLike, GroupPostComment
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


# Group posts handle classes


class GroupPostsClass:

    def add(self, user, groupName, content):
        group = get_object_or_404(Group, name=groupName)
        member = GroupMembers.objects.filter(group=group, user=user)
        manager = GroupManager.objects.filter(manager=user,group=group)
        if member.exists() or manager.exists():
            if group:
                create = GroupPost.objects.create(user=user,group=group,content=content)
                create.save()
                return True
        else:
            return group
        
    
    def get_posts(self, groupName):
        group = get_object_or_404(Group, name=groupName)
        posts = GroupPost.objects.filter(group=group).order_by('created_at')
        return posts

    
    def update(self, id, user, groupName, content):
        group = Group.objects.get(name=groupName)
        post = GroupPost.objects.get(id=id)
        group = GroupManager.objects.get(group=group)
        if post.user == user or group.manager == user:
            post.content = content
            post.save()
            return True
        else:
            return None
        
    
    def delete(self, id, user, groupName):
        group = Group.objects.get(name=groupName)
        post = GroupPost.objects.get(id=id)
        group = GroupManager.objects.get(group=group)
        if post.user == user or group.manager == user:
            post.delete()
            return True
        else:
            return None



class GroupPostLikeClass:

    def __init__(self, user, id):
        self.user = user
        self.id = id


    def identify(self):
        post = GroupPost.objects.get(id=self.id)
        try:
            like = GroupPostLike.objects.get(user=self.user,post=post)
            like.delete()
        except ObjectDoesNotExist:
            return self.create()
    

    def create(self):
        post = GroupPost.objects.get(id=self.id)
        like = GroupPostLike.objects.create(user=self.user,post=post)
        like.save()

    
    def delete(self):
        post = GroupPost.objects.get(id=self.id)
        like = GroupPostLike.objects.create(user=self.user,post=post)
        like.delete()


    def likes(self):
        post = GroupPost.objects.get(id=self.id)
        likes = GroupPostLike.objects.filter(post=post)
        return len(likes)
  


class GroupPostCommentClass:

    def comment(self, user, id, commentContent):
        post = get_object_or_404(GroupPost, id=id)
        if post:
            comment = GroupPostComment.objects.create(user=user,post=post,comment=commentContent)
            comment.save()
            return True

    
    def comments(self, id):
        post = get_object_or_404(GroupPost, id=id)
        if post:
            comments = GroupPostComment.objects.filter(post=post)
            return comments


    def delete(self, user, commentId):
        comment = get_object_or_404(GroupPostComment, user=user, id=commentId)
        if comment:
            comment.delete()
            return True
            

