from ..models import FeedPost
from django.shortcuts import get_object_or_404


# Feed Posts


class FeedPostClass:

    def create(self, user, content):
        post = FeedPost.objects.create(user=user,content=content)
        post.save()


    def view(self, user):
        posts = FeedPost.objects.filter(user=user)
        return posts

    
    def update(self, user, content, id):
        post = get_object_or_404(FeedPost, id=id, user=user)
        if post:
            post.content = content
            post.save()
            return post


    def delete(self, user, id):
        post = get_object_or_404(FeedPost, id=id, user=user)
        if post:
            post.delete()
            return True


