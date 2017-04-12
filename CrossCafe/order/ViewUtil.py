"""
Here we maintain the Util methods which is being used in the view.py
"""
import json
from . import OrderStatus
from datetime import datetime
from . import Util
from . import OrderDao
from order.models import Order
from django.http import JsonResponse


class ViewUtil(object):

    @staticmethod
    def get_items_from_placeorder_page(request, order):
        item_details = request.POST.get('cartdetail')
        order.order_items = item_details
        amount = ViewUtil.calculate_item_amount(item_details)
        order.amount = amount
        extra_charges = ViewUtil.calculate_tax(amount)+ViewUtil.calculate_extra_charges(amount)
        order.extra_charges = extra_charges
        order.delivery_charges = ViewUtil.calculate_delivery_charges(amount+extra_charges)
        order.total_amount = amount+extra_charges+order.delivery_charges
        address = str(request.POST.get('address1'))+str(request.POST.get('address2'))+str(request.POST.get('landmark'))
        order.delivery_address = address#request.POST.get('delivery_address')
        order.order_name = request.POST.get('order_name')
        order.status = OrderStatus.OrderStatus.DRAFT
        #order.customer_id = request.POST.get('customer_id')
        order.restaurant_id = request.POST.get('restaurant_id')
        order_type = request.POST.get('order_type')
        order.order_type = "ONLINE" if Util.Util.is_null(order_type) else order_type
        print order.customer_id
        order.last_update_by = order.customer_id#request.POST.get('customer_id')
        order.last_update_date = datetime.now()
        return order

    @staticmethod
    def calculate_item_amount(item_details):
        total_amount = 0
        print "in calculate_item_amount"
        print item_details
        if item_details is None or item_details == '' or item_details == '[]':
            return total_amount
        else:
            #data = json.dumps(item_details)
            #items = json.loads(str(item_details))
            items = eval(item_details)
            print items[0]
            if items is not None:
                for each_item in items:
                    total_amount += int(ViewUtil.get_item_price(each_item))
            else:
                return total_amount
        return total_amount

    #Gets the item price from Restaurant module for each item and calculate and return it
    @staticmethod
    def get_item_price(each_item):
        item_id = each_item['id']
        item_quantity = each_item['quantity']
        item_price = each_item['price']
        if item_id is None or item_quantity is None or item_price is None:
            raise ValueError('Item Id or Quantity cannot be null')
            item_price = 0
        # MenuModule.get_item_price(item_id)
        else:
            item_price = float(item_price) * float(item_quantity)
        return item_price

    @staticmethod
    def calculate_tax(amount):
        tax = amount * 0.15 #hard coded to 15% tax charges
        return tax

    @staticmethod
    def calculate_delivery_charges(amount):
        if amount>500:
            delivery_charges = 0
        delivery_charges = 50 #hard coded to 50 rupees
        return delivery_charges

    @staticmethod
    def calculate_extra_charges(amount):
        extra_charges = amount * 0.05 #hard coded to 15% tax charges
        return extra_charges

    @staticmethod
    def get_items_from_payment_page(request, order):
        #if request.POST.get('amount') is None:
            #raise ValueError('amount cannot be null!')
        #if request.POST.get('extra_charges') is None:
            #raise ValueError('extra_charges cannot be null!')
        payment_type = request.POST.get('paymenttype')
        print payment_type
        if payment_type is None:
            raise ValueError('payment_type cannot be null!')

        #order.amount = request.POST.get('amount')
        #d_charge = request.POST.get('delivery_charges')
        #order.delivery_charges = 0 if Util.Util.is_null(d_charge) else d_charge
        #order.extra_charges = request.POST.get('extra_charges')
        order.payment_type = payment_type
        order.status = OrderStatus.OrderStatus.AWAITING_ACCEPTANCE
        #if payment_type.upper() == "ONLINE_PAYMENT":
        order.bill_date = datetime.now()
        return order

    @staticmethod
    def get_payment_json_response(order):
        json = dict()
        json["order_id"] = order.order_id
        json["payment_status"] = "SUCCESS"
        json["order_status"] = order.status
        json["paid_amount"] = int(order.amount)+int(order.extra_charges)+int(order.delivery_charges)
        json["bill_date"] = order.bill_date
        json["order_id"] = order.order_id
        json["delivery_address"] = order.delivery_address
        json["customer_id"] = order.customer_id
        json["restaurant_id"] = order.restaurant_id
        return json

    @staticmethod
    def get_customer_id(request):
        customer_id = request.POST.get('customer_id')
        if customer_id is None or customer_id == '':
            customer_id = ViewUtil.register_customer(request)
        return customer_id

    #get the customer details from request and register a customer and return customer id
    @staticmethod
    def register_customer(request):
        json = dict()
        json["customer_fname"] = request.POST.get("fname")
        json["customer_lname"] = request.POST.get("lname")
        json["customer_email_id"] = request.POST.get("emailid")
        json["customer_contact_number"] = request.POST.get("mnumber")
        # Call the register API (with above payload) from user management module to register
        # the user, which should return the unique customer id for registered customer
        return request.POST.get("emailid")

    @staticmethod
    def prepare_order(request, customer_id):
        order_id = request.POST.get('order_id')
        order_dao = OrderDao.OrderDao.getInstance()
        #order = order_dao.find_by_id(order_id)
        if order_id is None or order_id == '':
            order = Order()
            order.customer_id = customer_id
            order = ViewUtil.get_items_from_placeorder_page(request, order)
            order_dao.insert(order)
        else:
            order = order_dao.find_by_id(order_id)
            order.customer_id = customer_id
            order = ViewUtil.get_items_from_placeorder_page(request, order)
            order_dao.update(order)
        return order