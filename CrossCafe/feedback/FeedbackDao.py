from .models import Complaint
from . import Util
from django.shortcuts import get_object_or_404, Http404

class FeedbackDao(object):

	def get_all_orders(self):
        return Complaint.objects.all()

    def find_by_id(self, order_id):
        if(Util.Util.is_null(order_id)):
            raise ValueError('order_id cannot be null!')
        order = Complaint.objects.filter(order_id=order_id).first()
        print "order",order,order_id
        return order


