from django.db import models
from django.contrib.auth.models import User


# Create your models here.


GENDER = (
    ('men', 'men'),
    ('women', 'women'),
    ('none', 'none'),
)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public = models.BooleanField(default=False)
    gender = models.CharField(max_length=5, choices=GENDER, default='none')
    birthday = models.DateField()
    phone = models.IntegerField()
    living = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = '1. Profile'


class ProfileWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workplace = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    detail = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = '2. Profile - Work'


class ProfileStudy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    detail = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = '3. Profile - Academic'


class Friends(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    friends = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '4. Friends'


class Group(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    about = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = '5. Groups'


class GroupManager(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    super_manager = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '6. Groups Managers'

        
class GroupMembersRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    by_manager = models.BooleanField(default=False)
    approve = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '7. Group Members Request'


class GroupMembers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '8. Group Members'


class GroupManagerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = '9. Group Manager Requests'


class GroupPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'A10. Group Posts'


class GroupPostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(GroupPost, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'A11. Post Likes'


class GroupPostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(GroupPost, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        verbose_name_plural = 'A12. Post comments'


class FeedPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'A13. Feed Posts'   


