from ..models import Group ,GroupManager
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


# Group Management


class GroupsManagmentClassTest:

    def create(self, user, name, about):
        try:
            Group.objects.get(name=name)
            return None
        except ObjectDoesNotExist:
            return GroupsManagmentClass().save(user, name, about)


    def get(self, user):
        groups = GroupManager.objects.filter(manager=user)
        return groups

    
    def update(self, user, name, about, id):
        group = get_object_or_404(Group, id=id)
        manager = get_object_or_404(GroupManager, manager=user, group=group)
        if group and manager:
            return GroupsManagmentClass().change(name, about, group.id)
        else:
            return group


    def delete(self, user, id):
        try:
            group = Group.objects.get(id=id, created_by=user)
            group.delete()
            return True
        except ObjectDoesNotExist:
            try:
                manager = GroupManager.objects.get(manager=user,group=id)
                if manager.super_manager == True:
                    group = Group.objects.get(id=id)
                    group.delete()
                    return True
                else:
                    return None
            except ObjectDoesNotExist:
                return None



class GroupsManagmentClass:

    def save(self, user, name, about):
        group = Group.objects.create(created_by=user,name=name,about=about)
        group.save()
        get_last = Group.objects.last()
        manager = GroupManager.objects.create(manager=user, group=get_last, super_manager=True)
        manager.save()
        return True


    def change(self, name, about, whichGruop):
        gruop = Group.objects.get(id=whichGruop)
        gruop.name, gruop.about = name, about
        gruop.save()
        return True
            
