from .models import UserProfile

class UserDetails(object):

    def getUserType(self,request):
        print request.user
        if(request.user.is_authenticated()):
            user = UserProfile.objects.get(user=request.user).user_type
        else:
            user = ""
        print user
        return user
