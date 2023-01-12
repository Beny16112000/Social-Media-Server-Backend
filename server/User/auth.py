from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


# User Test and Authentication System


class UserTest:

    success = True

    def register(self, username, fname, lname, email, password1, password2):
        if self.username(username) is True and self.email(email) is True and self.passwords(password1, password2) is True:
            return UserClass().create(username, fname, lname, email, password1)
        else:
            return {
                'username': self.username(username),
                'email': self.email(email),
                'password': self.passwords(password1,password2)
            }


    def username(self, username):
        try:
            User.objects.get(username=username)
            return 'Username already exist !'
        except ObjectDoesNotExist:
            return self.success

    
    def email(self, email):
        try:
            User.objects.get(email=email)
            return 'Email already exist !'
        except ObjectDoesNotExist:
            return self.success

    
    def passwords(self, pass1, pass2):
        if pass1 != pass2:
            return 'Psswords does Not match !'
        else:
            return self.success

    
    def login(self, username, password):
        try:
            getUser = User.objects.get(username=username)
            token = Token.objects.get(user=getUser)
            return token
        except ObjectDoesNotExist:
            user = authenticate(username=username, password=password)
            if user is not None:
                return UserClass().login(user)
            else:
                return {
                    'error': 'Username or password not match our data !'
                }


    def delete(self, userToken, pk):
        try:
            user, token = User.objects.get(id=pk), Token.objects.get(user=userToken)
            user.delete(), token.delete()
            return True
        except ObjectDoesNotExist:
            return {
                'message': 'Need to be authenticated'
            }



class UserClass:

    def create(self, username, fname, lname, email, password):
        user = User.objects.create_user(username, email, password)
        user.first_name, user.last_name, user.is_active = fname, lname, True
        user.save()
        return UserTest().success


    def login(self, user):
        token = Token.objects.create(user=user)
        token.save()
        return token


    def logout(self, username):
        user = User.objects.get(username=username)
        token = Token.objects.get(user=user)
        token.delete()
        return {
            'message': 'Logout'
        }








