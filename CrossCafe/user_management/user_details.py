from .models import UserProfile

class UserDetails(object):

    def getUserType(self,request):
        print request.user
        if(request.user.is_authenticated()):
            user = UserProfile.objects.get(user=request.user).user_type
        else:
            user = "attendant"
        # print user
        return "manager"


    def getDeliveryBoy(self, restaurant_id):
        DeliveryBoy=UserProfile.objects.filter(user_type="delivery_boy")
        return DeliveryBoy
            
