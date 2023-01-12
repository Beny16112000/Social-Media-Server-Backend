from ..models import GroupManagerRequest, GroupManager, Group, GroupMembers, GroupMembersRequest
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


# Group for manager requests handle


class ManagerRequest:

    def send(self, superuser, receiver, group):
        get_group = Group.objects.get(id=group)
        user = User.objects.get(id=receiver)
        try:
            GroupManager.objects.get(manager=user,group=get_group)
            return 404
        except ObjectDoesNotExist:
            check_request = GroupManagerRequest.objects.filter(user=user,group=get_group)
            if not check_request:
                check_superuser = get_object_or_404(GroupManager, manager=superuser, super_manager=True)
                if check_superuser:
                    request = GroupManagerRequest.objects.create(user=user,group=get_group)
                    request.save()
                    return True
            else:
                return 404

        
    def get(self, receiver):
        requests = GroupManagerRequest.objects.filter(user=receiver)
        return requests

    
    def update(self, user, id):
        request = get_object_or_404(GroupManagerRequest, id=id)
        if request:
            add = GroupManager.objects.create(manager=user, group=request.group)
            add.save()
            request.delete()
            return True
        else:
            return request


    def delete(self, user, id):
        request = get_object_or_404(GroupManagerRequest, id=id)
        if request:
            request.delete()
            return True

        
            
class GroupMembersClass:

    def send(self, user, groupId):
        group = Group.objects.get(id=groupId)
        try:
            GroupMembers.objects.get(user=user, group=group)
            return None
        except ObjectDoesNotExist:
            try:
                GroupManager.objects.get(manager=user, group=group)
                return None
            except ObjectDoesNotExist:
                try:
                    GroupMembersRequest.objects.get(user=user, group=group)
                except ObjectDoesNotExist:
                    request = GroupMembersRequest.objects.create(user=user,group=group)
                    request.save()
                    return True

            
    def view(self, user, groupId):
        group = Group.objects.get(id=groupId)
        try:
            GroupManager.objects.get(manager=user, group=group)
            requests = GroupMembersRequest.objects.filter(group=group)
            return requests
        except ObjectDoesNotExist:
            return None

    
    def update(self, requestId):
        request = GroupMembersRequest.objects.get(id=requestId)
        member = GroupMembers.objects.create(user=request.user,group=request.group)
        member.save()
        request.delete()


    def delete(self, requestId):
        request = GroupMembersRequest.objects.get(id=requestId)
        request.delete()

