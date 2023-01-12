from ..models import FeedPost, Friends
from django.db.models import Q
from ..serializer import FeedPostsSerializer


# Feed algorithm


class FeedAlgorithm:

    def algorithm(self, user):
        friends = Friends.objects.filter(Q(sender=user) | Q(receiver=user), friends=True)
        postsLi = []
        for i in friends:
            posts = FeedPost.objects.filter(Q(user=i.sender) | Q(user=i.receiver)).exclude(user=user).order_by('created_at')
            serializer = FeedPostsSerializer(posts, many=True)
            postsLi.append(serializer.data)
        return postsLi