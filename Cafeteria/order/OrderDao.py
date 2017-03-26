from .models import Order
from . import Util


class OrderDao(object):

    @staticmethod
    def getInstance():
        return OrderDao()

    def get_all_orders(self):
        return Order.objects.all()
        #Logic goes here to get all orders from order table and return as List of order

    def find_by_id(self, order_id):
        if(Util.Util.is_null(order_id)):
            raise ValueError('order_id cannot be null!')
        order = Order.objects.get(order_id=order_id)
        return order
        #Logic goes here to get an Order based on order Id
        #Make sure to validate the order_id(null check or any sanitization)

    def find_by_name(self, name):
        if(Util.Util.is_null(name)):
            raise ValueError('name cannot be null!')
        order = Order.objects.filter(order_name=name)
        return order
        # Logic goes here to get an Order based on order name from order table
        # Make sure to validate the name(null check or any sanitization)

    def find_by_customer_id(self, customer_id):
        if(Util.Util.is_null(customer_id)):
            raise ValueError('customer_id cannot be null!')
        order = Order.objects.filter(customer_id=customer_id)
        return order
        # Logic goes here to get an Order based on order name from order table
        # Make sure to validate the name(null check or any sanitization)

    def find_by_restaurant_id(self, restaurant_id):
        if(Util.Util.is_null(restaurant_id)):
            raise ValueError('restaurant_id cannot be null!')
            order = Order.objects.filter(restaurant_id=restaurant_id)
            return order
        # Logic goes here to get an Order based on order name from order table
        # Make sure to validate the name(null check or any sanitization)

    def insert(self, order):
        if Util.Util.is_null(order):
            raise ValueError('cannot insert null order!')
        order.save()
        return order
        #Insert the order into table here and return the new order obejct return from DB
        #Make sure of any kind of validation

    def delete(self, order):
        if Util.Util.is_null(order):
            raise ValueError('cannot delete null order!')
        if Util.Util.is_null(self.find_by_id(order.order_id)):
            raise ValueError('order does not exist in DB!')
        #Delete the order from table
        #Make sure of any kind of validation

    def update(self, order):
        if Util.Util.is_null(order):
            raise ValueError('cannot update null order!')
        if Util.Util.is_null(self.find_by_id(order_id = order.order_id)):
            raise ValueError('order does not exist in DB!')
        order.save()
        #Order.objects.filter(order_id=order.order_id).update(order) #check this
        return order
        #load the Order from DB by calling findById() and update the order
        #Make sure of validation whether the order exist or not or anyother validation