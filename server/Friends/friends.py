from ..models import Friends
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


# Freinds request handle


class FriendsClass:

    def send(self, sender, receiver):
        user = get_object_or_404(User, id=receiver)
        try:
            Friends.objects.get(Q(sender=sender) | Q(sender=user) | Q(receiver=user))
            return None
        except ObjectDoesNotExist:
            request = Friends.objects.create(sender=sender, receiver=user)
            request.save()
            return True


    def list(self, user):
        data = Friends.objects.filter(Q(friends=False),receiver=user)
        return data


    def accept(self, user, id):
        request = Friends.objects.get(receiver=user, id=id)
        request.friends = True
        request.save()
        return request

    
    def delete(self, user, id):
        request = Friends.objects.get(receiver=user,id=id,friends=False)
        request.delete()

    
    def all(self, user):
        friends = Friends.objects.filter(Q(sender=user) | Q(receiver=user), friends=True)
        return friends

    
    def delete_friendship(self, user, id):
        try:       
            friend = Friends.objects.get(Q(sender=user) | Q(receiver=user), friends=True, id=id)
            friend.delete()
            return True
        except ObjectDoesNotExist:
            return None


