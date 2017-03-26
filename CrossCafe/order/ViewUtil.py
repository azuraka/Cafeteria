from . import OrderStatus
from datetime import datetime
from . import Util
from django.http import JsonResponse
"""
Here we maintain the Util methods which is being used in the view.py
"""


class ViewUtil(object):

    @staticmethod
    def get_items_from_placeorder_page(request, order):
        item_details = request.POST.get('itemdetails')
        order.order_items = item_details
        order.amount = request.POST.get('amount')
        order.delivery_charges = request.POST.get('delivery_charges')
        order.extra_charges = request.POST.get('extra_charges')
        order.delivery_address = request.POST.get('delivery_address')
        order.order_name = request.POST.get('order_name')
        order.status = OrderStatus.OrderStatus.DRAFT
        order.customer_id = request.POST.get('customer_id')
        order.restaurant_id = request.POST.get('restaurant_id')
        order.order_type = request.POST.get('order_type')
        order.last_update_by = request.POST.get('customer_id')
        order.last_update_date = datetime.now()
        return order

    @staticmethod
    def get_items_from_payment_page(request, order):
        if request.POST.get('amount') is None:
            raise ValueError('amount cannot be null!')
        if request.POST.get('extra_charges') is None:
            raise ValueError('extra_charges cannot be null!')
        payment_type = request.POST.get('payment_type')
        if payment_type is None:
            raise ValueError('payment_type cannot be null!')

        order.amount = request.POST.get('amount')
        d_charge = request.POST.get('delivery_charges')
        order.delivery_charges = 0 if Util.Util.is_null(d_charge) else d_charge
        order.extra_charges = request.POST.get('extra_charges')
        order.payment_type = payment_type
        order.status = OrderStatus.OrderStatus.AWAITING_ACCEPTANCE
        if payment_type.upper() == "ONLINE_PAYMENT":
            order.bill_date = datetime.now()
        return order

    @staticmethod
    def get_payment_json_response(request, order):
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