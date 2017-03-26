from .models import Order
from . import Util
from django.shortcuts import get_object_or_404, Http404

class OrderDao(object):

    @staticmethod
    def getInstance():
        return OrderDao()

    def get_all_orders(self):
        return Order.objects.all()

    def find_by_id(self, order_id):
        if(Util.Util.is_null(order_id)):
            raise ValueError('order_id cannot be null!')
        order = Order.objects.filter(order_id=order_id).first()
        return order

    def find_by_name(self, name):
        if(Util.Util.is_null(name)):
            raise ValueError('name cannot be null!')
        order = Order.objects.filter(order_name=name)
        return order

    def find_by_customer_id(self, customer_id):
        if(Util.Util.is_null(customer_id)):
            raise ValueError('customer_id cannot be null!')
        try:
            order = Order.objects.filter(customer_id=customer_id)
        except Order.DoesNotExist:
            raise Http404("order does not exist")
        #Order.objects.get(customer_id=customer_id, offer_amount=False)
        return order

    def find_by_restaurant_id(self, restaurant_id):
        if(Util.Util.is_null(restaurant_id)):
            raise ValueError('restaurant_id cannot be null!')
        order = Order.objects.filter(restaurant_id=restaurant_id)
        return order

    def insert(self, order):
        if Util.Util.is_null(order):
            raise ValueError('cannot insert null order!')
        order.save()
        return order

    def delete(self, order):
        if Util.Util.is_null(order):
            raise ValueError('cannot delete null order!')
        if Util.Util.is_null(self.find_by_id(order.order_id)):
            raise ValueError('order does not exist in DB!')

    def update(self, order):
        if Util.Util.is_null(order):
            raise ValueError('cannot update null order!')
        if Util.Util.is_null(self.find_by_id(order_id = order.order_id)):
            raise ValueError('order does not exist in DB!')
        order.save()
        #Order.objects.filter(order_id=order.order_id).update(order) #check this
        return order