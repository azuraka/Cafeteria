"""
This file is to write the test cases related to APIs exposed from order module
"""

from django.test import TestCase, Client
from order import views
from order import OrderDao
from order.models import Order


class OrderAPITest(TestCase):

    @classmethod
    def setUp(self):
        self.client = Client()

    ORDER_NAME = "order_name"
    ORDER_ITEMS = "[{'item_id':'101','quantity':'2'},{'item_id':'102','quantity':'1'},{'item_id':'103','quantity':'3'},{'item_id':'104','quantity':'4'}]"
    STATUS = "DRAFT"
    RESTAURANT_ID = "101"
    ORDER_TYPE = "ONLINE"
    LAST_UPDATE_BY = "test"
    CUSTOMER_ID = "my_customer_id"

    def create_order(self):
        order = Order()
        order.order_name = self.ORDER_NAME
        order.order_items = self.ORDER_ITEMS
        order.status = self.STATUS
        order.restaurant_id = self.RESTAURANT_ID
        order.order_type = self.ORDER_TYPE
        order.last_update_by = self.LAST_UPDATE_BY
        order.customer_id = self.CUSTOMER_ID
        return order

    def test_place_order(self):
        order = self.create_order()
        order_dao = OrderDao.OrderDao.getInstance()
        order = order_dao.insert(order)
        print order.order_id
        payload = {}
        payload["amount"] = 200
        payload["extra_charges"] = 50
        payload["payment_type"] = "online"
        payload["delivery_charges"] = 50
        payload["order_id"] = order.order_id
        response = path = self.client.post('/cafeteria/order/pay',payload)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200, "placeorder API call test fail, dude, smells bad here!")
        print path

    def test_pay(self):
        order = self.create_order()
        order_dao = OrderDao.OrderDao.getInstance()
        order = order_dao.insert(order)
        payload = {}
        payload["cart"] = "[{'item_id':'101','quantity':'2'},{'item_id':'102','quantity':'1'},{'item_id':'103','quantity':'3'},{'item_id':'104','quantity':'4'}]"
        payload["restaurant_id"] = order.restaurant_id
        payload["order_type"] = "online"
        payload["customer_id"] = order.customer_id
        payload["order_id"] = order.order_id
        payload["order_name"] = "new order"

        response = path = self.client.post('/cafeteria/order/placeorder', payload)
        print path
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200, "payment API call test fail, dude, something fishy here!")

    def test_getcustomerorder(self):
        order = self.create_order()
        order_dao = OrderDao.OrderDao.getInstance()
        order = order_dao.insert(order)
        payload = {}
        payload["customer_id"] = order.customer_id
        response = path = self.client.post('/cafeteria/order/getcustomerorder', payload)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200, "getcustomerorder API call test fail, dude, something serious issue here!")

    def test_getrestaurantorder(self):
        order = self.create_order()
        order_dao = OrderDao.OrderDao.getInstance()
        order = order_dao.insert(order)
        payload = {}
        payload["restaurant_id"] = order.restaurant_id
        response = path = self.client.post('/cafeteria/order/getrestaurantorder', payload)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200, "getrestaurantorder API call test fail, dude, something serious issue here!")

    def test_getrestaurantorder_notexist(self):
        order = self.create_order()
        order_dao = OrderDao.OrderDao.getInstance()
        order = order_dao.insert(order)
        payload = {}
        payload["restaurant_id"] = "somerandomid"
        response = path = self.client.post('/cafeteria/order/getrestaurantorder', payload)
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200, "getrestaurantorder API call test fail, dude, something serious issue here!")