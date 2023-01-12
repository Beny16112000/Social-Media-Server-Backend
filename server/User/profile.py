from ..models import Profile, ProfileWork, ProfileStudy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


# Profile Class


class ProfileClass:
    success = True

    def main(self, user, public, gender, birthday, phone, living):
        if self.profile(user) is self.success:
            # If Public = 0 is True, If 1 is False
            if public == 0:
                public = True
            else:
                public = False
            profile = Profile.objects.create(user=user,public=public,gender=gender,birthday=birthday,phone=phone,living=living)
            profile.save()
            return self.success
        else:
            return {
                'profile': self.profile(user)
            }
            

    def profile(self, user):
        try:
            Profile.objects.get(user=user)
            return 'You alaredy have a profile'
        except ObjectDoesNotExist:
            return self.success
    

    def get(self, user):
        profile = Profile.objects.get(user=user)
        return profile

    
    def getWork(self, user):
        work = ProfileWork.objects.filter(user=user)
        return work

    
    def getStudy(self, user):
        study = ProfileStudy.objects.filter(user=user)
        return study

    
    def update(self, user, public, gender, birthday, phone, living):
        Profile.objects.filter(user=user).update(user=user,public=public,gender=gender,birthday=birthday,phone=phone,living=living)
        return True


    def delete(self, id):
        profile = Profile.objects.get(id=id)
        profile.delete()



class WorkNstudy:
    work = 1
    study = 2
    
    def create(self, user, place, start, end, detail, typeC):
        if typeC is self.work:
            user_offical = User.objects.get(username=user)
            work = ProfileWork.objects.create(user=user_offical,workplace=place,start=start,end=end,detail=detail)
            work.save()
            return True
        elif typeC is self.study:
            user_offical = User.objects.get(username=user)
            study = ProfileStudy.objects.create(user=user_offical,institution=place,start=start,end=end,detail=detail)
            study.save()
            return True
        else:
            return None

        
    def get(self, user, typeC):
        if typeC is self.work:
            work = ProfileWork.objects.filter(user=user)
            return work
        elif typeC is self.study:
            study = ProfileStudy.objects.filter(user=user)
            return study
    

    def delete(self, id, typeC):
        if typeC is self.work:
            work = ProfileWork.objects.get(id=id)
            work.delete()
        else:
            study = ProfileStudy.objects.get(id=id)
            study.delete()
